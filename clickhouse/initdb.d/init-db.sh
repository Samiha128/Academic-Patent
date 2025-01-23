SELECT *
 FROM s3(
    'http://minio:9000/journal/part-00000-e907300f-8f89-418a-9729-a8aee4f5cf3f-c000.snappy.parquet',  
-- URL du fichier S3
     'minio',  -- AWS_ACCESS_KEY_ID
     'minio123',  -- AWS_SECRET_ACCESS_KEY
     'Parquet'  -- Format du fichier
 )

 SELECT *
 FROM s3(
    'http://minio:9000/Author/part-00000-e907300f-8f89-418a-9729-a8aee4f5cf3f-c000.snappy.parquet',  
-- URL du fichier S3
     'minio',  -- AWS_ACCESS_KEY_ID
     'minio123',  -- AWS_SECRET_ACCESS_KEY
     'Parquet'  -- Format du fichier
 )


SELECT *
 FROM s3(
    'http://minio:9000/fact/part-00000-388c1a5f-dd39-4c9a-b00d-f910995b8a6f-c000.snappy.parquet',  
-- URL du fichier S3
     'minio',  -- AWS_ACCESS_KEY_ID
     'minio123',  -- AWS_SECRET_ACCESS_KEY
     'Parquet'  -- Format du fichier
 )

 SELECT *
 FROM s3(
    'http://minio:9000/journal/part-00000-87e821b6-08ff-49d6-9b36-91a0d26db8bc-c000.snappy.parquet',  
-- URL du fichier S3
     'minio',  -- AWS_ACCESS_KEY_ID
     'minio123',  -- AWS_SECRET_ACCESS_KEY
     'Parquet'  -- Format du fichier
 )