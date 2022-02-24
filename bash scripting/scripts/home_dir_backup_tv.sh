#!/bin/bash

# Author: Tracy Vierra
# Date Created: 1/31/2022
# Date Modified: 1/31/2022

# Description:
# This script will backup your home directory using tar and store the file in your home directory

# Usage:
# home_dir_backup.sh


tar -cvf ~/"$(date +%d-%m-%Y_%H-%M-%S)".tar ~/* 2>/dev/null

exit 0
