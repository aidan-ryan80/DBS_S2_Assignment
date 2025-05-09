FROM mariadb:10.3

# Install Python and dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libmariadb-dev

ENV MARIADB_ROOT_PASSWORD=rootpass

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN chmod +x /docker-entrypoint-initdb.d/run_python_init.sh

COPY Ski_Hotel_Init.py /docker-entrypoint-initdb.d/Ski_Hotel_Init.py
COPY run_init_py.sh /docker-entrypoint-initdb.d/run_init_py.sh

RUN chmod +x /docker-entrypoint-initdb.d/run_init_py.sh