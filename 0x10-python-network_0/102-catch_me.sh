#!/bin/bash
# This script displays the text "You got me!"
curl -s -X PUT -d "user_id=42" 0.0.0.0:5000/catch_me
