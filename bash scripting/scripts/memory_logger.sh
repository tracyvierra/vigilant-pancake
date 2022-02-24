#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/8/2022
# Date Modified: 2/8/2022

# Description:

# Usage:
# ./memory_logger.sh

if [ -d $HOME/performance ]; then
	echo "$HOME/performance directory exists"
else 
	echo "$HOME/performance directory does not exist"
	echo "creating $HOME/performance directory"
	mkdir $HOME/performance
fi

free >> $HOME/performance/memory.log

cat $HOME/performance/memory.log 






