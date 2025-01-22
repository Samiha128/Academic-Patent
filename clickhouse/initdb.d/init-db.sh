SELECT *
 FROM s3(
    'http://minio:9000/journal/part-00000-e907300f-8f89-418a-9729-a8aee4f5cf3f-c000.snappy.parquet',  
-- URL du fichier S3
     'minio',  -- AWS_ACCESS_KEY_ID
     'minio123',  -- AWS_SECRET_ACCESS_KEY
     'Parquet'  -- Format du fichier
 )
docker exec -it some-clickhouse-server clickhouse-client