import os
from minio import Minio
from minio.error import S3Error
client = Minio(
    "localhost:9000",  
    access_key="minio",  
    secret_key="minio123",  
    secure=False  
)
local_directory = r"..\..\jupylab\notebooks\data\Author"

if not client.bucket_exists("author"):
    client.make_bucket("author")

def upload_files(directory, bucket_name):
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            
            file_path = os.path.join(root, file)
            
            relative_path = os.path.relpath(file_path, directory)
            
            try:
              
                client.fput_object(bucket_name, relative_path, file_path)
                print(f"Uploaded {relative_path} to MinIO bucket '{bucket_name}'")
            except S3Error as err:
                print(f"Error uploading {relative_path}: {err}")
upload_files(local_directory, "author")
