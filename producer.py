#import tweepy
from tweepy import StreamingClient
from tweepy import StreamRule
from kafka import KafkaProducer
import logging

"""API ACCESS KEYS"""

consumerKey = ""
consumerSecret = ""
bearer_token = ""
accessToken = ""
accessTokenSecret = ""

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = 'twitter'
rules = StreamRule("#bitcoin")


def twitterAuth():
    # create the authentication object
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
    # set the access token and the access token secret
    authenticate.set_access_token(accessToken, accessTokenSecret)
    # create the API object
    api = tweepy.API(authenticate, wait_on_rate_limit=True)
    return api



class TweetListener(StreamingClient):
    def on_data(self, raw_data):
        logging.info(raw_data)
        producer.send(topic_name, value=raw_data)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

   
if __name__ == '__main__':
  while True:
    client = TweetListener(bearer_token)           
    client.add_rules(rules)
    client.filter()