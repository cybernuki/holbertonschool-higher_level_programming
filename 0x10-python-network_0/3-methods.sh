#!/bin/bash
# Display allowed methods of a URL
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
