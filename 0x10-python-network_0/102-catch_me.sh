#!/bin/bash
# catch the URL
curl -sL 0:5000/catch_me -XPUT -H"Origin: HolbertonSchool" -d"user_id=98"

