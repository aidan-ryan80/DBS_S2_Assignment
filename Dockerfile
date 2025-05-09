FROM mariadb:10.3

RUN apt-get update && \
    apt-get install -y python3 python3-pip libmariadb-dev build-essential && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY Ski_Hotel_Init.py .

# Override the default command to start MariaDB and run Python script
CMD ["sh", "-c", "/usr/local/bin/docker-entrypoint.sh mysqld & python3 /app/Ski_Hotel_Init.py && wait"]