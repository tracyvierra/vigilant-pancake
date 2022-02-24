#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/8/2022
# Date Modified: 2/8/2022

# Description:

# Usage:
# ./timer_project.sh -m <minutes> -s <seconds>

while getopts "m:s:" opt; do
	case "$opt" in
		m) # number of minutes
			minutes=$OPTARG
			;;
		s) # number of seconds
			seconds=$OPTARG
			;;
		\?)
			Echo "Invalid option provided"
	;;
	esac
	

done

total_seconds=$((minutes * 60 + seconds))
echo "Total seconds: $total_seconds"
echo 
while [ $total_seconds -ne 0 ]; do
	echo "$total_seconds seconds remaining"
	sleep 1
	total_seconds=$((total_seconds - 1))
done 
echo "Timer done at $(date +%m-%d-%Y_%H:%M:%S)!"





