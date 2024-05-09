#!/usr/bin/bash
# cURL body size
import sys
argv = sys.argv

curl -sI "$1" | grep 'Content-Length' | awk '{print $2}' 
