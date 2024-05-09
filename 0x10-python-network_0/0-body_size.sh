#!/bin/bash
# cURL body size

curl -sI "$0" | grep 'Content-Length' | awk '{print $2}' 
