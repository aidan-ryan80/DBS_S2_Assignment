FROM mariadb:10.3

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libmariadb-dev \
    dos2unix

ENV MARIADB_ROOT_PASSWORD=rootpass

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN chmod +x /docker-entrypoint-initdb.d/run_python_init.sh

COPY Ski_Hotel_Init.py /docker-entrypoint-initdb.d/Ski_Hotel_Init.py
COPY run_init_py.sh /docker-entrypoint-initdb.d/run_init_py.sh

RUN dos2unix /docker-entrypoint-initdb.d/run_init_py.sh && \
    chmod +x /docker-entrypoint-initdb.d/run_init_py.sh