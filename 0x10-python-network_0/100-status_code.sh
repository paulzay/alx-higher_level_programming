#!/bin/bash
# comment
curl -sI -w '%{response_code}' "$1" -o /dev/null
