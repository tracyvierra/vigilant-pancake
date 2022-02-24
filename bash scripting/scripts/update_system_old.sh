#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/16/2022
# Date Modified: 2/16/2022

# Description:
# This script will run apt-get update and dist-upgrade and reboot if a reboot is required.

# Usage: 
# ./update_system.sh 

apt-get update -y
apt-get dist-upgrade -y

if [ -f /var/run/reboot-required ]; then
         shutdown --reboot
fi








