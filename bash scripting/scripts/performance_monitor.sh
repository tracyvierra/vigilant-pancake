#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/16/2022
# Date Modified: 2/16/2022

# Description:

# Usage:

echo $(date) >> "$HOME"/performance_monitor.log 2>&1

ping -c 1 google.com &> /dev/null
	if [ "$?" -eq 0 ]; then
 		echo "Internet: Connected" >> "$HOME"/performance_monitor.log 2>&1
	else
 		echo "Internet: Disconnected" >> "$HOME"/performance_monitor.log 2>&1
fi

echo "RAM Usage :" >> "$HOME"/performance_monitor.log 2>&1 
free -h | grep "Mem" >> "$HOME"/performance_monitor.log 2>&1

echo "Swap Usage :" >> "$HOME"/performance_monitor.log 2>&1
free -h | grep "Swap" >> "$HOME"/performance_monitor.log 2>&1

echo "Disk Usage :" >> "$HOME"/performance_monitor.log 2>&1
df -h >> "$HOME"/performance_monitor.log 2>&1
echo "" >> "$HOME"/performance_monitor.log 2>&1




