import boto3
import os
from _02_config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME

def upload_to_s3(local_file, bucket_name, remote_path):
    try:
        #creo el cliente s3 con la libreria boto3 y las credenciales
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        
        #conecto al cliente s3 y subo el archivo
        s3_client.upload_file(local_file, bucket_name, remote_path)
        print(f"Archivo '{local_file}' subido como '{remote_path}' en el bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error al subir archivo a S3: {e}")



if __name__ == "__main__":
    #ruta al archivo json
    project_dir = os.path.dirname(os.path.abspath(__file__))
    local_file = os.path.join(project_dir, "raw_books.json")
        
    #ruta dentro del bucket S3
    remote_path = "raw_data/raw_books.json"

    # Subir el archivo al bucket de S3
    upload_to_s3(local_file, S3_BUCKET_NAME, remote_path)
