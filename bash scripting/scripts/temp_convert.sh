#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/8/2022
# Date Modified: 2/8/2022

# Description:

# Usage:
# ./temp_convert.sh <unit> <temp>


while getopts "c:f:" opt; do
	case "$opt" in
		c) # convert from celsius to farenheit
			result=$(echo "scale=2; ($OPTARG * (9 / 5)) + 32" | bc)
;;
		f) # convert from fahrenheit to celsius
			result=$(echo "scale=2; ($OPTARG - 32) * (5/9)" | bc)
;;
		\?)
			Echo "Invalid option provided"
;;
esac
echo "$result"
donewhile getopts "f:c:" opt; do
  case "$opt" in
    f)
      echo "fahrenheit"
      ;;
    c)
      echo "celsius"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done







