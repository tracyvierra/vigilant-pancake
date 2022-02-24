#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/11/2022
# Date Modified: 2/11/2022

# Description: 
# This script will create directories passed in from a file separated by a newline.

# Usage:
# ./read-while-project.sh <filename>

while read line; do
    mkdir "$(pwd)/testing/$line"
done < "$1"
echo " "
echo "Directories created in "$(pwd)"."
echo " "









