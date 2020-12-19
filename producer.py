from faker import Faker
from kafka import KafkaProducer
import json
import time

fake = Faker()

def MakeFakeData():
  return {
    'name': fake.name(),
    'address': fake.address(),
    'createdAt': int(fake.year())
  }

def jsonSerializer(data):
  return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
    value_serializer=jsonSerializer)

if __name__ == "__main__":
  while 1 == 1:
    registeredData = MakeFakeData()
    # print(registeredData)
    producer.send('registered-user', registeredData)
    time.sleep(1)