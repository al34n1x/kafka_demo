#from tweepy import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream
from kafka import KafkaProducer
from tweepy import StreamingClient
from tweepy import StreamRule
#import tweepy


producer = KafkaProducer(bootstrap_servers='localhost:9092')
accessToken = ""
accessTokenSecret = ""
bearer_token = ""
consumerKey = ""
consumerSecret = ""
topic_name = "twitter"
rules = StreamRule("#nerdearla")

class TweetListener(StreamingClient):
  def on_data(self, data):
    producer.send(topic_name, data) #str.encode(data))
    print(data)
    return True

  def on_error(self, status):
    print(status)
  
if __name__ == '__main__':
  while True:
    client = TweetListener(bearer_token)           
    client.add_rules(rules)
    client.filter()
    
