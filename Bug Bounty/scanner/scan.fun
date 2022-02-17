#!/bin/bash
nmap_scan()
{
 nmap $DOMAIN > $DIRECTORY/nmap
 echo "The results of nmap scan are stored in $DIRECTORY/nmap."
}
dirsearch_scan()
{
 $PATH_TO_DIRSEARCH/dirsearch.py -u $DOMAIN -e php --simple-report=$DIRECTORY/dirsearch
 echo "The results of dirsearch scan are stored in $DIRECTORY/dirsearch."
}
crt_scan()
{
 curl "https://crt.sh/?q=$DOMAIN&output=json" -o $DIRECTORY/crt
 echo "The results of cert parsing is stored in $DIRECTORY/crt."
}