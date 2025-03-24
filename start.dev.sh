#!/bin/bash

DOCKER_COMPOSE="docker compose --project-directory . -f contrib/container/dev-docker-compose.yml"

SKIP_SETUP=false
for arg in "$@"; do
    if [[ "$arg" == "--skip-setup" ]]; then
        SKIP_SETUP=true
        break
    fi
done

# Backend setup
if [ "$SKIP_SETUP" = false ]; then
    $DOCKER_COMPOSE run --rm inventree-dev-server invoke install
    $DOCKER_COMPOSE run --rm inventree-dev-server invoke dev.setup-test --dev
fi
$DOCKER_COMPOSE up -d

# Frontend setup
# https://github.com/inventree/InvenTree/blob/stable/docs/docs/develop/react-frontend.md
$DOCKER_COMPOSE run --rm inventree-dev-server sh -c "invoke int.frontend-install && invoke int.frontend-trans"
$DOCKER_COMPOSE run --rm -p 5173:5173 inventree-dev-server sh -c "cd src/frontend/ && yarn run dev --host"
