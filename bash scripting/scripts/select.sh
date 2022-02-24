#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/7/2022
# Date Modified: 2/7/2022

# Description:

# Usage:
# ./select.sh
PS3="What is the day of the week? "
select day in Monday Tuesday Wednesday Thursday Friday Saturday Sunday; do
	echo "Today is $day"
	break
done
PS3=" "
