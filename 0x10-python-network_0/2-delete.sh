#!/bin/bash
# Sends a DELETE request to the URL that is passed as a first argument and displays the body in responce.
curl -s -X DELETE "${1}"
