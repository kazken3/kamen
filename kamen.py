import sys
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

if(len(sys.argv[1] == 2):
    api.update_status(sys.argv[1])
    sys.exit(0);

matsuya = re.compile(u"松屋なう") 
matsuyanow = re.compile(u"#matsuyanow")
#print sys.argv[1]
q = "松屋なう"
for r in tweepy.Cursor(api.search,q,show_user = True).items(100):
    if matsuya.search(r.text) is not None:
        if matsuyanow.search(r.text): #matsuyanowしてたらいらない
            continue
        text = "#nantokanyau RT @"+r.from_user+" "+r.text
#        api.update_status(text)
        print r.from_user
        print r.text

api.update_status(sys.argv[1])


