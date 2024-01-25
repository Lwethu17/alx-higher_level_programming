#!/bin/bash
# Sends a JSON POST request to the URL passed as an argument and displays the body of response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
