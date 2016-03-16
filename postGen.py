#Import the necessary methods from tweepy library
import string
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import csv
import re


#Variables that contains the user credentials to access Twitter API 
access_token = "354977528-Yv0mv1324nDNSfaQtOywH2rdwU33XspDijTqS11u"
access_token_secret = "WYU2YPedx6xvgKEImhpJoIkxaUG0aSNEAvcrxvVW9wiAb"
consumer_key = "7bcckilEovSW2mLDb1DdmQKXx"
consumer_secret = "ETYQ9SQBYqK7lFHP1yu0fDMbniRLyohbxBgrc16qeBDYRzjCaH"


#This handles Twitter authetification and the connection to Twitter Streaming API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# read the file
with open('tweets.csv') as f:
	topic_id = 0
	for line in f:
		topic_id = topic_id + 1
		twt = api.get_status(line)
		while twt.in_reply_to_status_id <> None:
                    	p = re.compile(r'@\w*\b')
			txt = p.sub('', twt.text)
                        txt = filter(lambda x: x in string.printable, txt)
                        with open('reply.csv','a') as replyf:
			        replyf.write('{}, {}\n'.format(topic_id,txt))
                        print('append a reply')
                    	twt = api.get_status(twt.in_reply_to_status_id)
		p = re.compile(r'@\w*\b')
	    	txt = p.sub('', twt.text)
                txt = filter(lambda x: x in string.printable, txt)
                with open('topic.csv','a') as topicf:
    		        topicf.write('{}, {}\n'.format(topic_id,txt))
    		print('append a topic')
				


#twt = api.get_status(650978698624126976)
#print(twt.in_reply_to_screen_name)
