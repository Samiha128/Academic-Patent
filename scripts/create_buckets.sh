#!/bin/bash


sleep 20

mc alias set myminio http://192.168.16.2:9000 minio minio123

mc mb myminio/raw
mc mb myminio/silver
mc mb myminio/gold

echo "Buckets 'raw', 'silver', 'gold' créés avec succès !"
