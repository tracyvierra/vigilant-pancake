#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/11/2022
# Date Modified: 2/11/2022

# Description:

# Usage:

readarray -t urls < urls.txt

for url in "${urls[@]}"; do 
	curl --head $url -o $(echo $url | cut -d "." -f 2).txt 
	 
done



# their solution:

# readarray -t urls < urls.txt

# for url in "${urls[@]}"; do
#  webname=$(echo "$url" | cut -d . -f 2)
#  curl --head "$url" > "$webname.txt"
# done



