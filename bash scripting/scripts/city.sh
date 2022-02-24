#!/bin/bash

# Author: Tracy Vierra
# Date Created: 2/8/2022
# Date Modified: 2/8/2022

# Description:

# Usage:
# ./city.sh

select city in Tokyo "New York" London "Los Angeles" Moscow Dubai Manchester  Paris Bangalore Johannesburg Istanbul Milan "Abu Dhabi" Pune Nairobi Berlin Karachi
do
	echo "You selected "$city""
	break
done

case "$city" in 
	Tokyo)
		echo ""$city" is in Japan"
		;;
	"New York"|"Los Angeles")
		echo ""$city" is in the United States"
		;;
	London | Manchester)
		echo ""$city" is in the United Kingdom"
		;;
	Moscow)
		echo ""$city" is in Russia"
		;;
	Dubai|Bangalore|"Abu Dhabi"|Pune)
		echo ""$city" is in the United Arab Emirates"
		;;
	Paris)
		echo ""$city" is in the French Republic"
		;;
	Johannesburg)
		echo ""$city" is in South Africa"
		;;
	Istanbul)
		echo ""$city" is in Turkey"
		;;
	Milan)
		echo ""$city" is in the Italian Republic"
		;;
	Nairobi)
		echo ""$city" is in Kenya"
		;;
	Berlin)
		echo ""$city" is in the German Republic"
		;;
	Karachi)
		echo ""$city" is in Pakistan"
		;;
	
esac






