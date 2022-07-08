import json
from kafka import KafkaProducer

data = {"a": 1, "b": 2, "c":3}
producer = KafkaProducer(bootstrap_servers=["localhost:9092"],
                         api_version=(0, 10, 0),
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for i in range(1000):
    producer.send("test", data, partition=0)



from kafka import KafkaConsumer
consumer = KafkaConsumer('test',
                         group_id="group2",
                         bootstrap_servers=["localhost:9092"])
for msg in consumer:
    print(msg.value)