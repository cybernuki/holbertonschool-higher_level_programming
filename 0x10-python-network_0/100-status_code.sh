#!/bin/bash
# Shows only http status code
curl -s -o /dev/null -w "%{http_code}" "$1"
