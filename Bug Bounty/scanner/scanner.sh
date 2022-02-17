#!/bin/bash
source ./scan.func
PATH_TO_DIRSEARCH="/usr/bin/dirsearch"
getopts "m:" OPTION
MODE=$OPTARG
for i in "${@:$OPTIND:$#}"
do
 DOMAIN=$i
 DIRECTORY=${DOMAIN}_recon
 echo "Creating directory $DIRECTORY."
 mkdir $DIRECTORY

 case $MODE in
 nmap-only)
 nmap_scan
 ;;
 dirsearch-only)
 dirsearch_scan
 ;; 
 crt-only) 
 crt_scan
 ;;
 *) 
 nmap_scan
 dirsearch_scan
 crt_scan
 ;; 
 esac
 echo "Generating recon report for $DOMAIN..."
 TODAY=$(date)
 echo "This scan was created on $TODAY" > $DIRECTORY/report
 if [ -f $DIRECTORY/nmap ];then
 echo "Results for Nmap:" >> $DIRECTORY/report
 grep -E "^\s*\S+\s+\S+\s+\S+\s*$" $DIRECTORY/nmap >> $DIRECTORY/report
 fi
 if [ -f $DIRECTORY/dirsearch ];then
 echo "Results for Dirsearch:" >> $DIRECTORY/report
 cat $DIRECTORY/dirsearch >> $DIRECTORY/report
 fi
 if [ -f $DIRECTORY/crt ];then
 echo "Results for crt.sh:" >> $DIRECTORY/report
 jq -r ".[] | .name_value" $DIRECTORY/crt >> $DIRECTORY/report
 fi
done
