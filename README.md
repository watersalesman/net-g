Net-G
==
Net-G is a daemon that will send system network information such as IP addresses to the user via a Gmail account. This is useful when it is necessary to know a device's IP address but static IPs and dynamic DNS are not an option, e.g. college campus or other shared network.

The Python script will use your Gmail account to send an email to itself, containing your public IP address and the output of *ifconfig*.

The script is written for Python 3 and the daemon is written in C++.


Installation
--
Ensure that Python 3 is installed.

Then run:
```
git clone https://github.com/watersalesman/net-g.git
cd net-g
sudo sh netg.install
```

Afterward, configure Net-G by running:
```
sudo netg-pref
```

*The Gmail account and password will be saved as plaintext in the config file.* Although the file is only accessible by root, consider creating an account or using a junk account for security purposes. The config file will be stored as */etc/netg/netg.conf*

Writen for Arch Linux at the momement. However, it is simple enough that you should be able to make it work on another distro by just changing the method of service startup. I will still continue to work on making it more proper and compatible with other distros.

Usage
--
You can activate the systemd service *netg.service* to have it run on startup.

Example for Arch:
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
