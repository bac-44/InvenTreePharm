#!/bin/bash
docker compose --project-directory . -f contrib/container/dev-docker-compose.yml run --rm inventree-dev-server invoke migrate
