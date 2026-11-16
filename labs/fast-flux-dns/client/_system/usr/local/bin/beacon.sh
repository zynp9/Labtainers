#!/bin/bash
while true; do
   dig +short cdn.redpill.lab
   echo "$(date +%T) looked up"
   sleep $((40 + RANDOM % 20))     # waits 40–59 seconds
done