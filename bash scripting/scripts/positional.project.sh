#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/3/2022
# Date Modified: 2/4/2022

# Description:
# This script will calculate the positional parameters of a command line using the first positional parameter as the operand

# Usage:
# positional.project.sh [operand] [number1] [number2] [number3] [number4] [number5] [number6] [number7] [number8] [number9]

# My solution:
# echo "$(($2 $1 $3 $1 $4 $1 $5 $1 $6 $1 $7 $1 $8 $1 $9 $1 $10))"

# Solution with method to allow blank positional parameters:
echo $(( ${2:-0} $1 ${3:-0} $1 ${4:-0} $1 ${5:-0} $1 ${6:-0} $1 ${7:-0} $1 ${8:-0} $1 ${9:-0} $1 ${10:-0} ))

