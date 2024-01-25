#!/bin/bash
# Sends a request to the URL and dsplays the size of the body in responce
curl -s "${1}" | wc -c
