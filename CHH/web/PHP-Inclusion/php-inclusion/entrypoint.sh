#!/bin/bash

# Secure entrypoint
chmod 600 /entrypoint.sh

flag=$(cat /flag.txt) && \
  flag_escaped=$(echo "$flag" | sed 's/"/\\\\"/g') && \
  sed -i "2s/$/ \'$flag_escaped\'; /" /www/uploads/flag.php

exec "$@"