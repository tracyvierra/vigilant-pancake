#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/16/2022
# Date Modified: 2/17/2022

# Description:
# This script will run apt-get update and dist-upgrade, also autoremove and autoclean and reboot if a reboot is required.
# a log will be created in the $HOME directory of root since you have to run the script with sudo.

# Usage: 
# sudo ./update_system.sh 

update_system () {
        apt-get update -y
        apt-get dist-upgrade -y
        apt-get autoremove -y
        apt-get autoclean -y
        if [ -f /var/run/reboot-required ]; then
                shutdown --reboot
        fi
}
#
#
{ 
        echo "Updating System on $(date)"
        echo " "
        update_system 
        echo " "
        echo "Update System Complete on $(date)"
        echo "_____________________________________________"
        echo " "
}  >> "$HOME"/update_system_"$(hostname)".log 2>&1








