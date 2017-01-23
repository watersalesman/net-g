#!/usr/bin/python3
import smtplib
import shlex
from subprocess import Popen, PIPE

def get_command_output(command):
    args = shlex.split(command)
    process = Popen(args, stdout=PIPE)
    raw_out = process.communicate()[0]
    return raw_out.decode('utf-8')

def pseudo_grep(text, filter_string):
    output = ''
    for line in text.split("\n"):
        if filter_string in line:
            output += line + "\n"
    return output

class Gmail():
    def __init__(self, login, pw):
        self._login = login
        self._pw = pw
        self._server = smtplib.SMTP('smtp.gmail.com:587')

    def get_login(self):
        return self._login

    def get_pw(self):
        return self._pw

    def get_server(self):
        return self._server

    def authenticate(self):
        print('\nAuthenticating...')
        self._server.ehlo()
        print('Greeted server successfully')
        self._server.starttls()
        print('Started TLS')
        self._server.login(self.get_login(), self.get_pw())
        print('Logged in!')

    def quit_server(self):
        self._server.quit()

    def send_email(self, to_addr,msg, subject):
        from_addr = self.get_login()
        message = 'Subject: %s\n\n%s' % (subject, msg)
        print('\nSending email...')
        self._server.sendmail(from_addr, to_addr, message)
        print('Sent!\n')

def main():

    #File that will be checked for changes
    ip_info_path = '/etc/netg/ip.info'

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
    #If there is no file, we will set prev_info as blank and create a file later
    try:
        with open(ip_info_path, 'r') as ip_info_file:
            prev_info = ip_info_file.read()
    except FileNotFoundError:
        prev_info = ''

    #Get current network info to use for comparison
    current_info = "Public IP: " + get_command_output('curl -s https://now-dns.com/ip')
    current_info += "\n" + pseudo_grep(get_command_output('ifconfig'), 'inet')

    #If ip.info does not match the current status of 'ifconfig'
    if prev_info != current_info:
        try:
            #Authenticate Gmail credentials
            gmail = Gmail(email, passw)
            gmail.authenticate()

            #Send the Public IP and output from 'ifconfig'
            email_body = "Public IP: " + get_command_output('curl -s https://now-dns.com/ip')
            email_body += "\n\n" + get_command_output('ifconfig')
            gmail.send_email(gmail.get_login(), email_body, device)
            gmail.quit_server()
            print('Sleeping...')

            #Write current network info to ip.info for future checks
            with open(ip_info_path, 'w') as ip_info:
                ip_info.write(current_info)
        except:
            print('Failed to authenticate')
            print('Check your internet connection and ensure \
                    that your Gmail credentials are correct.')
            print('Sleeping...')
    else:
        print('No changes detected.')
        print('Sleeping...')


if __name__ == '__main__':
    main()
