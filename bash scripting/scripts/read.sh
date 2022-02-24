#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/7/2022
# Date Modified: 2/7/2022

# Description:
# read in data and save as variables, then print back out.

# Usage:
# ./read.sh

# echo "Enter your name, age, and town : "
read -t 15 -p "Please enter your name : " name
read -s -t 15 -p "Please enter your age : " age
read -t 15 -p "Please enter your town : " town

echo "Your name is $name, you are $age years old, and you live in $town."








