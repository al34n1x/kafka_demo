import json 
from kafka import KafkaConsumer
from pymongo import MongoClient

try:
   # connect = MongoClient('mongodb://root:root@localhost:27017')
    connect = MongoClient('mongodb://localhost:27017')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

def main():

    consumer = KafkaConsumer('messages',
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest')
    db = connect.sample
    collection = db.data
    for msg in consumer:
        output = []
        output.append(json.loads(msg.value))
        collection.insert_one(json.loads(msg.value))
        print (json.loads(msg.value))
        print ('\n')


if __name__ == "__main__":
    main()

