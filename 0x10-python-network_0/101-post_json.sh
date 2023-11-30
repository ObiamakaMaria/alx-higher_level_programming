#!/bin/bash
# This script sends a JSON POST to the server & displays response
curl -s -X POST -H 'Content-Type: application/json' -d @"$2" "$1"
