#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
curl "$1" -siX OPTIONS | grep "Allow" | cut -d ':' -f 2 | cut -c 2-
