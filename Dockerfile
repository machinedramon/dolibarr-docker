FROM monogramm/docker-dolibarr:13.0-apache

# Instalar Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Instalar bibliotecas Python necessárias (exemplo: requests)
RUN pip3 install requests

# Copiar o script Python para o contêiner
COPY ./custommodule/scripts/myscript.py /var/www/html/custom/custommodule/scripts/myscript.py
