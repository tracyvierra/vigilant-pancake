#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/8/2022
# Date Modified: 2/8/2022

# Description:
# This script will illustrate test fucntions nad errror codes.

# Usage:
# ./test.sh

a=$(cat file1.txt) # "a" equals contents of file1.txt
b=$(cat file2.txt) # "b" equals contents of file2.txt
c=$(cat file3.txt) # "c" equals contents of file3.txt
if [ "$a" = "$b" ] && [ "$a" = "$c" ]; then
rm file2.txt file3.txt
else
echo "File1.txt did not match both files"
fi








