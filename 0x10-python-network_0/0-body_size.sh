#!/bin/bash
# This script GETS the length of the content body 
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
