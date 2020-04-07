#!/bin/bash
# Send a post using the JSON format
curl -s "$1" -XPOST -H "Content-Type: application/json" -d "$(cat "$2")"

