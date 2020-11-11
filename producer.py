from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
topic_name = "twitter"
class StdOutListener(StreamListener):
  def on_data(self, data):
    producer.send(topic_name, str.encode(data))
    print(data)
    return True

  def on_error(self, status):
    print(status)
  
if __name__ == '__main__':
  while True:
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['#BTC', '#btc', '#bitcoin', '#BITCOIN', '#Bitcoin'],languages=["en"])
               
