#!/bin/sh

# Sleeping 10 seconds to let PostgreSQL and MariaDB start and be ready to connect
echo "Sleeping for 10 seconds to let PostgreSQL and MariaDB start..."
sleep 10

echo "Starting pgloader migration..."
# Run pgloader
pgloader /mnt/migrate.load