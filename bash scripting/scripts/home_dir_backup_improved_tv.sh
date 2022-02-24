#!/bin/bash

# Author: Tracy Vierra
# Date Created: 1/31/2022
# Date Modified: 1/31/2022

# Description:
# This script will backup your home directory using tar and store the file in your current directory

# Usage:
# home_dir_backup_improved_tv.sh

currentdir=$(pwd)

echo "Hello, ${USER^}!"
echo "I will now back up your home directory, $HOME"
echo  ""
echo "You are running this script from ${currentdir}"
echo "Therefore, I will save the file in the current directory: ${currentdir}"

tar -cf ${currentdir}/"$(date +%d-%m-%Y_%H-%M-%S)".tar $HOME/* 2>/dev/null

echo  ""

echo "Backup Completed Successfully."

exit 0
