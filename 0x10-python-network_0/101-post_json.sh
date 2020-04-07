#!/bin/bash
# Shows only http status code
curl -s "$1" -XPOST -H "Content-Type: application/json" -d "$(cat "$2")"

