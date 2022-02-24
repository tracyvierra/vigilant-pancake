#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/16/2022
# Date Modified: 2/17/2022

# Description:
# This script will run apt-get update and dist-upgrade, also autoremove and autoclean and reboot if a reboot is required.
# a log will be created in the $HOME directory of root since you will need to use suso to run the script.

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
 
echo "Updating System on $(date)" | tee -a "$HOME"/update_system_"$(hostname)".log
echo " " | tee -a "$HOME"/update_system_"$(hostname)".log
update_system | tee -a "$HOME"/update_system_"$(hostname)".log 
echo " " | tee -a "$HOME"/update_system_"$(hostname)".log
echo "Update System Complete on $(date)" | tee -a "$HOME"/update_system_"$(hostname)".log
echo "_____________________________________________" | tee -a "$HOME"/update_system_"$(hostname)".log
echo " " | tee -a "$HOME"/update_system_"$(hostname)".log









