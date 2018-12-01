#!/bin/bash

INPUT=$(<input)
FREQ=0
USED=()

while true; do
  while read -r p; do
    FREQ=$(($FREQ$p))

    if [[ " ${USED[*]} " == *" $FREQ "* ]]; then
      echo "Yeeeey: $FREQ"
      echo -e "\a"
      break 2
    fi

    USED+=($FREQ)
  done <<< "$INPUT"
  echo "Next round"
done
