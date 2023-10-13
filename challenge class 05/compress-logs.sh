#!/bin/bash
#Script:    Ops Challenge 05
#Author:    Tiago Godinho
#Date of latest revision:   13/10/2023
#Purpose    Compressing and clearing logs

#Variables
syslog=/var/log/syslog
syslogsize=$(stat -c%s "$syslog")
wtmp=/var/log/syslog
wtmpsize=$(stat -c%s "$wtmp")
syslogbck=/var/log/backups/syslog
syslogbcksize=$(stat -c%s "$syslog")
wtmpbck=/var/log/backups/wtmp
wtmpsizebck=$(stat -c%s "$wtmp")

#Create log backups folder
mkdir -p /var/log/backups

#Print syslog filesize
echo "Size of $syslog = $syslogsize bytes."
#Print wtmp filesize
echo "Size of $wtmp = $wtmpsize bytes."

#Compress syslog file and copy it to backups folder
gzip -c "$syslog" > "$syslogbck-$(date '+%Y%m%d%H%M%S').zip"
#Compress wtmp file and copy it to backups folder
gzip -c "$wtmp" > "$wtmpbck-$(date '+%Y%m%d%H%M%S').zip"

#Clear content of syslog file
: > "$syslog"
#Clear content of syslog file
: > "$syslog"

#Print compressed syslog filesize
echo "Size of $syslogbck = $syslogsizebck bytes."
#Print compressed wtmp filesize
echo "Size of $wtmpbck = $wtmpsizebck bytes."