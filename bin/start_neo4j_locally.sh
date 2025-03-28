#!/bin/zsh
# https://neo4j.com/docs/operations-manual/current/docker/introduction

if [ ! -d "neo4j/data" ]; then
    mkdir -p neo4j/data
fi

if [ ! -d "neo4j/logs" ]; then
    mkdir -p neo4j/logs
fi

docker run \
    --restart=always \
    --publish=7474:7474 --publish=7687:7687 \
    --user="$(id -u):$(id -g)" \
    --volume="$(pwd)/neo4j/data:/data" \
    --volume="$(pwd)/neo4j/logs:/logs" \
    --env NEO4J_AUTH=none \
    --env NEO4J_PLUGINS='["graph-data-science"]' \
    neo4j:2025.02.0