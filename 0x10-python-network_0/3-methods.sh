#!/bin/bash
# This script lists all allowed methods accepted by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2- 
