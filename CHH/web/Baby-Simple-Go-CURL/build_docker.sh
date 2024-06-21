#!/bin/bash
docker rm -f ssrf-015
docker build --tag=ssrf-015 .
docker run -p 1337:1337 --rm --name=ssrf-015 ssrf-015