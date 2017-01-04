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

    def authenticateGmail(self):
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
    ipInfoPath = '/home/userpc/.config/netg/ip.info'

    try:
        with open('/home/userpc/.config/netg/netg.conf', 'r') as config:
            email = config.readline()[:-1]
            passw = config.readline()[:-1]
            config.readline()
            device = config.readline()[:-1]
    except FileNotFoundError:
        print('No configuration file was found. Please run "netg-pref".')
        print('Exiting...')
        return -1

    try:
        with open(ipInfoPath, 'r') as ipInfoRead:
            currentip = ipInfoRead.read()
    except FileNotFoundError:
        currentip = ''

    if currentip != pseudoGrep(getCommandOutput('ifconfig'), 'inet'):
        try:
            gmail = Gmail(email, passw)
            gmail.authenticateGmail()
            gmail.sendEmail(gmail.getLogin(), getCommandOutput('ifconfig'), device)
            gmail.quitServer()
            print('Sleeping...')
            with open(ipInfoPath, 'w') as ipinfo:
                ipinfo.write(pseudoGrep(getCommandOutput('ifconfig'), 'inet'))
        except:
            print('Failed to authenticate')

    else:
        print('No changes detected.')
        print('Sleeping...')


if __name__ == '__main__':
    main()
