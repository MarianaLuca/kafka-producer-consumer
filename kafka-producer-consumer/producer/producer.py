from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime
import os
import time

producer = KafkaProducer(
    bootstrap_servers=[os.getenv("SERVER_KAFKA")],
    api_version=(0, 11, 5),
    value_serializer=lambda v: str(v).encode("utf-8"),
)

while True:
    time.sleep(5)
    r = random.randint(1, 999)
    print("Number generate " + str(r))
    producer.send("kafka-python-topic", r)

