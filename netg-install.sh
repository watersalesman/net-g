#!/bin/bash
echo 'g++ -o netg-d netg-d.cpp'
g++ -o netg-d netg-d.cpp
echo
install -m 644 netg.service /usr/lib/systemd/system/netg.service
install -m 744 netg-pref.sh /usr/bin/netg-pref
install -m 744 netg.py /usr/bin/netg
install -m 744 netg-d /usr/bin/netg-d
echo
echo 'Enable "netg.service" for daemon'
echo 'or run "netg" for single use'
echo
echo 'IMPORTANT: Run "netg-pref" to initialize configuration'
echo files, otherwise Net-G will fail to run properly
echo
