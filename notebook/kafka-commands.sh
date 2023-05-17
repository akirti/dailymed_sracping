#!/bin/bash
echo "Creating Topic dailymeds on your local Kafka Server"
docker compose exec broker \
  kafka-topics --create \
    --topic dailymeds \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1