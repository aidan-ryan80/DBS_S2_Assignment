#!/bin/sh

# Sleeping 15 seconds to let PostgreSQL and MariaDB start and be ready to connect
echo "Sleeping for 15 seconds to let PostgreSQL and MariaDB start..."
sleep 15

echo "Starting pgloader migration..."
# Run pgloader
pgloader /mnt/migrate.load