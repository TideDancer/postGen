#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import csv
from multiprocessing import Pool
from multiprocessing import Process
import time

#Variables that contains the user credentials to access Twitter API 
access_token = "354977528-Yv0mv1324nDNSfaQtOywH2rdwU33XspDijTqS11u"
access_token_secret = "WYU2YPedx6xvgKEImhpJoIkxaUG0aSNEAvcrxvVW9wiAb"
consumer_key = "7bcckilEovSW2mLDb1DdmQKXx"
consumer_secret = "ETYQ9SQBYqK7lFHP1yu0fDMbniRLyohbxBgrc16qeBDYRzjCaH"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def __init__(self, keyword):
        self.keyword = keyword
    
    def on_data(self, data):
        tweets_data = json.loads(data)
	if tweets_data['in_reply_to_user_id'] <> None:
		with open('tweets_{}.csv'.format(self.keyword),'a') as f:
			f.write(tweets_data['id_str']+'\n')
		print('add one')
        return True

    def on_error(self, status):
        print status

def newThread(keyword):
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(keyword)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[keyword])
   

if __name__ == '__main__':
    
    keywordList=['python', 'food', 'javascript', 'ruby', 'news', 'life','work','museum','flower','computer',
                'security','science','game','football','nature']
    for i in range(0,5):
        print keywordList[i]
        p = Process(target = newThread, args=('{}'.format(keywordList[i]),))
        p.start()
        p.join()
        print(p.pid)
        time.sleep(5)
        p.terminate()


    #api = tweepy.API(auth)
    #user = api.get_user(887360983)
    #twt = api.get_status(650978698624126976)
    #print(twt.in_reply_to_screen_name)
