#!/bin/bash
SITES=(www.bluepill.lab cdn.bluepill.lab)
while true; do
   site=${SITES[$RANDOM % ${#SITES[@]}]}
   dig +short $site
   echo "$(date +%T) looked up $site"
   sleep $((10 + RANDOM % 10))
done