#!/bin/bash
# Sends a request to the URL passed as an argument and displays the status code of the responce.
curl -so /dev/null -w "%{http_code}" "$1"
