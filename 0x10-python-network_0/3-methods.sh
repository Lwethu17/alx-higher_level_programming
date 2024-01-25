#!/bin/bash
# Displays all of the HTTPS methods the server will accept.
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
