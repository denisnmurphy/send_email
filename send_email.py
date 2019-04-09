import email.utils
from email.mime.text import MIMEText
import time
# Import smtplib (to allow us to email)
import smtplib

# set the 'from' address,
fromaddr = 'myemail@gmail.com'
# set the email password
password = 'myemailpassword'
# set the 'to' addresses,
toaddrs = ['someperson@hotmail.com']


# Message body
text = '''
Some email text goes here. Or it could be html but will need to pass html attr to MIMEText.
'''

def send_email(delay_time=0):
    time.sleep(delay_time)
    print('Sending email...')
    # Loop through send to addresses
    for to in toaddrs:
        msg = MIMEText(text)  # Get message ready in email format
        msg.set_unixfrom('author')
        msg['To'] = email.utils.formataddr(('Recipient', to))
        msg['From'] = email.utils.formataddr(('My Name', fromaddr))
        msg['Subject'] = 'Hello'

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login(fromaddr, password)

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(to))
        print('Message: ' + msg.as_string())

        # send the email
        server.sendmail(fromaddr, to, msg.as_string())
        # disconnect from the server
        server.quit()
        print('Email has been sent!')

send_email(delay_time=10)
