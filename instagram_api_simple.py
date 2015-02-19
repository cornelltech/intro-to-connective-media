#! /usr/bin/python

# Simple Instagram example
# Make sure to git clone https://github.com/Instagram/python-instagram into the directory you are working on.

import sys
#import simplejson as json
from instagram.client import InstagramAPI
from instagram import InstagramAPIError
from datetime import datetime


client_id     = "XXXXX"
client_secret = "YYYYYY"
access_token  = "ZZZZZ"

CRAWL_RADIUS        = 5000

def crawl_locations(points):
    api = InstagramAPI(access_token=access_token)

    for point in points:
        print("Media search for %s,%s"%(point['lat'],point['lng']))
        try:
            crawled_media = api.media_search(lat=point['lat'],lng=point['lng'], distance=CRAWL_RADIUS)
        except InstagramAPIError as ie:
            print("Instagram API error" + str(ie))
            return
        except Exception as e:
            print("General exception" + str(e))
            return
        
        for media in crawled_media:
            print media, media.user, media.images['thumbnail'].url
            print "++"

        print ("Got %d results\n"%len(crawled_media))

        if len(crawled_media) > 0:
            latest_id   = crawled_media[0].id
            print "Latest result ID:", latest_id


def crawl_own():
    api = InstagramAPI(access_token=access_token)

    try:
        #recent_media, next_ = api.user_recent_media(user_id="mmoorr", count=10)
        media_feed, next_ = api.user_media_feed(count=20)
    except InstagramAPIError as ie:
        print("Instagram API error" + str(ie))
        return
    except Exception as e:
        print("General exception" + str(e))
        return

    for media in media_feed:
        print media.user
        if media.caption:
            print media.caption.text
        print "++"

def crawl_all_feeders():
    api = InstagramAPI(access_token=access_token)

    try:
        #recent_media, next_ = api.user_recent_media(user_id="mmoorr", count=10)
        media_feed, next_ = api.user_media_feed(count=20)
    except InstagramAPIError as ie:
        print("Instagram API error" + str(ie))
        return
    except Exception as e:
        print("General exception" + str(e))
        return
    
    crawled={}
    for media in media_feed:
        if media.user.id in crawled: continue
        crawled[media.user.id] = True
        try:
            recent_media, next_ = api.user_recent_media(user_id=media.user.id, count=10)
            user_info           = api.user(user_id=media.user.id)
        except InstagramAPIError as ie:
            print("Instagram API error" + str(ie))
            return
        except Exception as e:
            print("General exception" + str(e))
            return
        print ("Got %d items for user %s"%(len(recent_media), media.user))
        print ("This is %s, ID %s, bio %s, followed by %s"%(user_info.full_name, 
                                                            user_info.id, 
                                                            user_info.bio, 
                                                            user_info.counts['followed_by']))
        print ("++")

if __name__ == '__main__':

    if (len(sys.argv) != 3):
        print "No argument, getting my own photos!"
        crawl_own()
        crawl_all_feeders()
    else:
        lat, lng = float(sys.argv[1]), float(sys.argv[2])
        crawl_locations([{"lat" : lat, "lng" : lng}])
    

