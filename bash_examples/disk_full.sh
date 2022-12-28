#!/bin/bash
#check if any disk is over 75% in use, and if so print an alert
usage=$(df -H -x squashfs -x tmpfs -x devtmpfs | grep dev | awk '{print $5}' | tr -d %)
IFS=$'\n'
for num in $usage; do
  if [[ "$num" -ge 75 ]]; then
    echo "Disk Usage Critical!"
    exit 1
  fi
done
