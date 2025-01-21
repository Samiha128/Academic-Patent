 
## Kafka

This project sets up a local Kafka environment using Docker Compose with two main services: Zookeeper and Kafka. Zookeeper is used for managing Kafka's metadata, while Kafka handles real-time data streaming. The configuration in the docker-compose.yml file defines the listening ports, service connections, and settings required to run a Kafka cluster. This setup is used to extract data from Scopus via a Kafka cluster running in a Docker container.

##  How to Run the Project

### Set Up Docker Desktop on Your PC
Ensure that Docker Desktop is installed on your computer. You can download it from the official Docker website ,After installing, make sure Docker Desktop is running.
### Start the Services with Docker Compose

Run the following command to start the Kafka and Zookeeper services in detached mode
 ```bash
docker-compose up -d
```
Once the services are up and running, you can create the Kafka topic with:
```bash
docker-compose exec kafka kafka-topics --create --topic scopus --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:29092
```

### Run the Kafka Producer
fter creating the topic, you can run the producer using the Python script:
python producer.py

###  Run the Kafka Consumer
you can run the consumer using the Python script:
python consumer.Py
