<h1>Instruções de Uso do Script</h1>

<p>bucket_name: Substitua pelo nome do bucket S3 existente onde deseja enviar os arquivos.</p>
<p>diretorio_fotos: Ajuste o caminho para o diretório onde suas fotos estão armazenadas, aqui está configurado para a área de trabalho do usuário (~/Desktop/xxx).
</p>
Este script verificará se o diretório de fotos existe e fará o upload de cada arquivo encontrado para o bucket S3 especificado. Certifique-se de que os arquivos no diretório são válidos antes de executar o upload.

<h3>Requisitos</h3>
<p>Python 3</p>
pip install boto3
<p></p>
Boto3 Doc: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

<h3>AWS credentials</h3>

[default]
<p></p>
aws_access_key_id = ACCESS_KEY
<h3></h3>
aws_secret_access_key = SECRET_KEY


<h3>AWS CONFIG </h3>
[default] 
<p></p>
region = us-east-1

<h3>Run</h3>
python main.py

