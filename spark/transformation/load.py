from minio import Minio
from minio.error import S3Error
import os

minio_client = Minio(
    'localhost:9000',
    access_key='minio',
    secret_key='minio123',
    secure=False
)

def list_buckets():
    try:
        buckets = minio_client.list_buckets()
        print("Buckets existants dans MinIO :")
        for bucket in buckets:
            print(bucket.name)
    except S3Error as err:
        print("MinIO error: ", err)

def download_files_in_bucket(bucket_name, output_dir):
    try:
        objects = minio_client.list_objects(bucket_name, recursive=True)

        for obj in objects:
            file_key = obj.object_name
            local_file_path = os.path.join(output_dir, file_key)

           
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

            
            try:
                response = minio_client.get_object(bucket_name, file_key)
                with open(local_file_path, 'wb') as file_data:
                    for d in response.stream(32*1024):
                        file_data.write(d)
                response.close()
                response.release_conn()
                print(f"Fichier téléchargé avec succès depuis MinIO vers {local_file_path}")

            except S3Error as err:
                print("MinIO error: ", err)

    except S3Error as err:
        print("MinIO error: ", err)

list_buckets()

download_files_in_bucket('raw', 'spark/data')