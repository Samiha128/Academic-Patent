#!/bin/bash
pip install requests python-dotenv confluent-kafka
# Lancer un topic (exemple : création d'un topic)
docker-compose exec kafka kafka-topics --create --topic scopus --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:29092
# Lancer un consumer pour consommer les messages du topic
docker-compose exec kafka kafka-console-consumer --topic scopus --from-beginning --bootstrap-server localhost:29092