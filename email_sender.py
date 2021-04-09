from smtplib import SMTP

HOST = 'smtp.gmail.com'
PORT = 587    
SENDER = 'example@gmail.com'
PASSWORD = 'password'

server = SMTP(host=HOST, port=PORT)

server.connect(host=HOST, port=PORT)

server.ehlo()
server.starttls()
server.ehlo()  

server.login(user=SENDER, password=PASSWORD)

RECIPIENT = 'reve172020@gmail.com'

MESSAGE = '''
Hi! from Python 
'''

server.sendmail(SENDER, RECIPIENT,MESSAGE)
