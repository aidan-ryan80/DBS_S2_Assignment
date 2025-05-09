FROM mariadb:10.3

RUN apt-get update && \
    apt-get install -y python3 python3-pip libmariadb-dev build-essential && \
    apt-get clean

WORKDIR /app

ENV MARIADB_ROOT_PASSWORD=rootpass

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN chmod +x /docker-entrypoint-initdb.d/run_python_init.sh

COPY Ski_Hotel_Init.py .

EXPOSE 3306

# Override the default command to start MariaDB and run Python script
CMD ["sh", "-c", "/usr/local/bin/docker-entrypoint.sh mysqld & python3 /app/Ski_Hotel_Init.py && wait"]