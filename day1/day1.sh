#!/bin/bash

INPUT=$(<input)
FREQ=0
declare -A ARR
ARR[$FREQ]=0

while true; do
  while read -r p; do
    FREQ=$(($FREQ$p))

    if [[ ${ARR[$FREQ]} ]]; then
      echo "Yeeeey: $FREQ"
      echo -e "\a"
      break 2
    fi

    ARR[$FREQ]="$p"
  done <<< "$INPUT"
  echo "Next round"
done
