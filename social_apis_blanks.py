1. Generate an oauth token by:
curl -i -u your_username -d '{"scopes": ["repo", "gist", "notifications", "user"], "note": "getting-started"}' https://api.github.com/authorizations
or by going to: https://github.com/settings/tokens/new (select all but the admin categories and delete_repo)
2. Check access:
curl -i -H 'Authorization: token GITHUB_TOKEN' https://api.github.com/user
3. Browse to docs: http://pygithub.readthedocs.org/en/stable/github.html and https://developer.github.com/v3/

# view user repos
curl -i -H 'Authorization: token GITHUB_TOKEN' https://api.github.com/___1

# view user owned repos
curl -i -H 'Authorization: token GITHUB_TOKEN' https://api.github.com/___2

# repo events
curl -i -H 'Authorization: token GITHUB_TOKEN' https://api.github.com/___3

# repo push events
curl -i -H 'Authorization: token GITHUB_TOKEN' https://api.github.com/___4

###########################
# PYTHON  (requires PyGithub)

from github import Github
g = Github('GITHUB_TOKEN')

# get user info
u = g.___5
# print raw user info
print u.___6
# print user id, name, number of public repos
print ___7

# get user repos
for repo in ___8:
	# print repo name
    print ___9

# get specific repo activity
for e in ___10.get_events():
	# print event time, user and type
    print ___11

###########################
# Instagram
1. Go to https://www.instagram.com/developer create app, uncheck implicit premission
2. Browse to https://api.instagram.com/oauth/authorize/?client_id=<CLIENT_ID>&redirect_uri=http://localhost&response_type=token&scope=basic+likes+comments+follower_list+public_content
3. Check access: 
curl https://api.instagram.com/v1/users/self/?access_token=INSTAGRAM_TOKEN
Alternatively, get token from https://apigee.com/embed/console/instagram
4. Browse to docs: https://github.com/Instagram/python-instagram and https://www.instagram.com/developer/endpoints/

# apigee
api = InstagramAPI(access_token="INSTAGRAM_TOKEN")

# get user info
u = ___12
# print user id, username, full name
print ___13
# print activity counts
print ___14

# get followers
followers, next_ = api.___15
while next_:
    more_followers, next_ = api.user_followed_by(with_next_url=next_)
    followers.extend(more_followers)

# get followees
followees, next_ = api.___16
while next_:
    more_followees, next_ = api.___17(with_next_url=next_)
    followees.extend(more_followees)

# intersect followers and followees 
set([f.username for f in followers]) & set([f.username for f in followees])

# get user feed
media_feed, next_ = api.___18(count=20)
for media in media_feed:
	# print media's user 
    print ___19
    # print caption
    if ___20:
        print ___20
    print "++"

# get followed people media and info
crawled={}
for media in media_feed:
    if media.user.id in crawled: 
    	___21
    crawled[media.user.id] = True
    # friend's recent media
    recent_media, next_ = api.user_recent_media(___1, count=10)
    # friend's info
    user_info           = api.user(___2)
    # print number of media elements
    print ("Got %d items for user %s"%(len(recent_media), media.user))
    # print user full name, id, bio, number of followers
    print ("This is %s, ID %s, bio %s, followed by %s"%(user_info.full_name, 
                                                        user_info.id, 
                                                        user_info.bio, 
                                                        user_info.counts['followed_by']))
    print ("++")

# search public content posted around a geo-location (cornell tech)
crawled_media = api.media_search(___3=40.741, ___3=-74.002)
print "Got %d results\n" % len(crawled_media)