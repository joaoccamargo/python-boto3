import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os

def upload_arquivo(bucket_name, file_path, file_name):
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(file_path, bucket_name, file_name)
        print(f'Arquivo {file_name} carregado com sucesso no bucket {bucket_name}!')
    except NoCredentialsError:
        print("Credenciais AWS não encontradas. Verifique suas configurações.")
    except PartialCredentialsError:
        print("Credenciais AWS incompletas. Verifique suas configurações.")
    except Exception as e:
        print(f'Erro ao fazer upload do arquivo: {e}')

if __name__ == "__main__":
    bucket_name = 'BUCKET S3 NOME'
    diretorio_fotos = os.path.expanduser('~/Desktop/fotos')
    
    if not os.path.exists(diretorio_fotos):
        print(f'O diretório {diretorio_fotos} não existe.')
    else:
        
        for foto in os.listdir(diretorio_fotos):
            file_path = os.path.join(diretorio_fotos, foto)
            if os.path.isfile(file_path):
                upload_arquivo(bucket_name, file_path, foto)
            else:
                print(f'{file_path} não é um arquivo válido.')