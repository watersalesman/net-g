#!/usr/bin/python3
import smtplib
import shlex
from subprocess import Popen, PIPE

def getCommandOutput(command):
    args = shlex.split(command)
    process = Popen(args, stdout=PIPE)
    rawOut = process.communicate()[0]
    return rawOut.decode('utf-8')

def pseudoGrep(text, filterStr):
    output = ''
    for line in text.split("\n"):
        if filterStr in line:
            output += line + "\n"
    return output

class Gmail():
    def __init__(self, login, pw):
        self._login = login
        self._pw = pw
        self._server = smtplib.SMTP('smtp.gmail.com:587')

    def getLogin(self):
        return self._login

    def getPw(self):
        return self._pw

    def getServer(self):
        return self._server

    def authenticate(self):
        print('\nAuthenticating...')
        self._server.ehlo()
        print('Greeted server successfully')
        self._server.starttls()
        print('Started TLS')
        self._server.login(self.getLogin(), self.getPw())
        print('Logged in!')

    def quitServer(self):
        self._server.quit()

    def sendEmail(self, toaddr,msg, subject):
        fromaddr = self.getLogin()
        message = 'Subject: %s\n\n%s' % (subject, msg)
        print('\nSending email...')
        self._server.sendmail(fromaddr, toaddr, message)
        print('Sent!\n')

def main():

    #File that will be checked for changes
    ipInfoPath = '/etc/netg/ip.info'

    #Read from config file
    try:
        with open('/etc/netg/netg.conf', 'r') as config:
            email = config.readline()[:-1]
            passw = config.readline()[:-1]
            config.readline()
            device = config.readline()[:-1]
    except FileNotFoundError:
        print('No configuration file was found. Please run "netg-pref".')
        print('Sleeping...')
        return -1

    #Check ip.info for network info
    #If there is no file, we will set previnfo as blank and create a file later
    try:
        with open(ipInfoPath, 'r') as ipInfoRead:
            previnfo = ipInfoRead.read()
    except FileNotFoundError:
        previnfo = ''

    #Get current network info to use for comparison
    currentinfo = "Public IP: " + getCommandOutput('curl -s https://now-dns.com/ip')
    currentinfo += "\n" + pseudoGrep(getCommandOutput('ifconfig'), 'inet')

    #If ip.info does not match the current status of 'ifconfig'
    if previnfo != currentinfo:
        try:
            #Authenticate Gmail credentials
            gmail = Gmail(email, passw)
            gmail.authenticate()

            #Send the Public IP and output from 'ifconfig'
            emailbody = "Public IP: " + getCommandOutput('curl -s https://now-dns.com/ip')
            emailbody += "\n\n" + getCommandOutput('ifconfig')
            gmail.sendEmail(gmail.getLogin(), emailbody, device)
            gmail.quitServer()
            print('Sleeping...')

            #Write current network info to ip.info for future checks
            with open(ipInfoPath, 'w') as ipinfo:
                ipinfo.write(currentinfo)
        except:
            print('Failed to authenticate')
            print('Sleeping...')
    else:
        print('No changes detected.')
        print('Sleeping...')


if __name__ == '__main__':
    main()
