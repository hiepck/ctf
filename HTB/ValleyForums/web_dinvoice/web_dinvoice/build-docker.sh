#!/bin/bash
docker rm -f web_dinvoice
docker build -t web_dinvoice .
docker run --name=web_dinvoice --rm -p1337:1337 -it web_dinvoice