import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
#Access to url and get PIN code.
print 'Please authorize: ' + auth_url
#Input PIN code
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
#Get ACCESS_KEY and ACCESS_SECRET
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret


