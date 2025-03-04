#!/bin/bash
docker compose --project-directory . -f contrib/container/docker-compose.yml build
docker compose --project-directory . -f contrib/container/docker-compose.yml up -d
docker compose --project-directory . -f contrib/container/docker-compose.yml run --rm inventree-server invoke update --skip-backup
