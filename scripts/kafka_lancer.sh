#!/bin/bash

docker-compose exec kafka kafka-topics --create --topic scopus --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:29092
