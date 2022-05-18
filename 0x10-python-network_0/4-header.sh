#!/bin/bash
# script that takes in a URL as an argument
curl -s -X GET "$1" -H "X-School-User-Id:98"
