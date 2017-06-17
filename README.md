Net-G
==
NOTE: This program is easily replaced by using a Dynamic DNS service and updating it to a private IP address. This was something I used before figuring this out. I simply fleshed it out to get practice with GitHub and maintaining software through this platform. One may, however, wish to use this in place of DDNS for security reasons as you would not be making private network information public. Other than that, a DDNS service and ddclient is more convenient.

Net-G is a daemon that will send system network information such as IP addresses to the user using a Gmail account. This is useful in situations where it is necessary to know a device's IP address but static IPs and DDNS are not an option, e.g. a college campus or other shared network.

The Python script will use your Gmail account to send an email to itself, containing your public IP address and the output of *ifconfig*.

The script is written for Python 3 and the daemon is written in C++.


Installation
--
Ensure that Python 3 is installed.

Then run:
```
git clone https://github.com/watersalesman/net-g.git
cd net-g
sudo sh netg-install.sh
```

Afterward, configure Net-G by running:
```
sudo netg-pref
```
To uninstall simply run the *netg-uninstall.sh* script as root.

*The Gmail account and password will be saved as plaintext in the config file.* Although the file is only accessible by root, consider creating an account or using a junk account for security purposes. The config file will be stored as */etc/netg/netg.conf*

Usage
--
You can activate the systemd service *netg.service* to have it run on startup.
```
#Enable netg.service
sudo systemctl enable netg

#Start netg.service
sudo systemctl start netg
```

Or you can run the following for single uses:
```
sudo netg
```
