#!/bin/bash
echo "Removing any present Net-G services..."
systemctl stop netg.service
systemctl disable netg.service
cp netg.service /usr/lib/systemd/system/netg.service
cp netg-pref.sh /usr/bin/netg-pref
cp netg.py /usr/bin/netg
echo
echo 'g++ -o /usr/bin/netg-d netg-d.cpp'
g++ -o /usr/bin/netg-d netg-d.cpp
echo
chmod +x /usr/bin/netg-d
chmod +x /usr/bin/netg-pref
chmod +x /usr/bin/netg
chmod 744 /usr/bin/netg-d
chmod 744 /usr/bin/netg-pref
chmod 744 /usr/bin/netg
echo
echo 'Enable "netg.service" for daemon'
echo 'or run "netg" for single use'
echo
echo 'IMPORTANT: Run "netg-pref" to initialize configuration'
echo files, otherwise Net-G will fail to run properly
echo
