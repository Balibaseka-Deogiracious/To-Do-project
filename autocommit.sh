#!/usr/bin/env bash

# Append a timestamp to the activity log, then commit and push changes every 2 minutes.
while true
do
  echo "Update at $(date)" >> activity_log.txt
  git add .
  git commit -m "Auto commit update" || true
  git push || true
  sleep 120
done
