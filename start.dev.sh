#!/bin/bash
docker compose --project-directory . -f contrib/container/dev-docker-compose.yml run --rm inventree-dev-server invoke install
docker compose --project-directory . -f contrib/container/dev-docker-compose.yml run --rm inventree-dev-server invoke dev.setup-test --dev
docker compose --project-directory . -f contrib/container/dev-docker-compose.yml up -d
