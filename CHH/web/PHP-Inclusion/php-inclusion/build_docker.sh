#!/bin/bash
chal="${CHAL:-path-traversal-005}"
docker rm -f "$chal"
docker build --tag="$chal" .
docker run -p 1337:1337 --rm --name="${chal}" "${chal}"