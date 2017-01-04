#!/bin/bash
conffolder="$HOME/.config/netg"
conffile="$conffolder/netg.conf"

echo This will overwrite any credentials
echo present in /etc/netg/netg.conf.
echo
echo Please input your Gmail credentials.
echo
echo Email:
read email
echo
echo Password:
read pass
echo
echo 'How often would you like Net-G to check for changes? (in seconds)'
read checktime
echo
echo "What would you like to name this device (this will appear on the email subject line)?"
read device
echo

if [ ! -d "$conffolder"  ]; then
	mkdir -p "$conffolder"
fi

echo $email > "$conffile"
echo $pass >> "$conffile"
echo $checktime >> "$conffile"
echo $device >> "$conffile"
echo > $conffolder/ip.info
chmod -R 700 $conffolder
