#!/usr/bin/env bash

mapfile -t file2 < file2

max=${#file2[@]}

while read line; do
  ((count++))
  echo "$line"
  if [[ $((count%2)) == 0 ]]; then
    if [[ next -ge max ]]; then
      next=0
    fi
    echo "${file2[next++]}"
  fi
done < file1
~              
