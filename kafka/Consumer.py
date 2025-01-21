from confluent_kafka import Consumer, KafkaException, KafkaError
from minio import Minio
from minio.error import S3Error
import io
import json
import uuid

kafka_config = {
    'bootstrap.servers': 'localhost:29092',  
    'group.id': 'mygroup1',  
    'auto.offset.reset': 'earliest'  
}

consumer = Consumer(kafka_config)
topic_name = 'scopus' 
consumer.subscribe([topic_name])

minio_client = Minio(
    'localhost:9000',  
    access_key='minio',  
    secret_key='minio123',  
    secure=False  
)

bucket_name = 'raw' 

if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)

try:
    while True:
        msg = consumer.poll(1.0)  
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        message_value = msg.value()
        print(f"Received message: {message_value.decode('utf-8')}")

       
        object_name = (msg.key().decode('utf-8') if msg.key() else str(uuid.uuid4())) + '.json'
        data = io.BytesIO(message_value) 
        minio_client.put_object(bucket_name, object_name, data, len(message_value))

except S3Error as err:
    print(f"MinIO error: {err}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
