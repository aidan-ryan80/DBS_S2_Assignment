FROM mariadb:10.3

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libmariadb-dev \
    dos2unix

ENV MARIADB_ROOT_PASSWORD=rootpass

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ski_hotel_init.py /docker-entrypoint-initdb.d/ski_hotel_init.py
COPY ski_hotel_init_wrapper.sh /docker-entrypoint-initdb.d/ski_hotel_init_wrapper.sh

EXPOSE 3306

RUN dos2unix /docker-entrypoint-initdb.d/ski_hotel_init_wrapper.sh && \
    chmod +x /docker-entrypoint-initdb.d/ski_hotel_init_wrapper.sh