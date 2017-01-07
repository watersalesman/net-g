#!/bin/bash
systemctl stop netg
systemctl disable netg
rm -f /usr/lib/systemd/system/netg.service
rm -f /usr/bin/netg
rm -f /usr/bin/netg-d
rm -f /usr/bin/netg-pref
rm -rf /etc/netg

