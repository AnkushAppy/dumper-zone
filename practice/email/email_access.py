import imapclient
import pyzmail
import pprint
from BeautifulSoup import BeautifulSoup



def login_mail_server():
	imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
	USER_EMAIL = raw_input("Enter your email address: ")
	USER_PASSWORD = raw_input("Enter your password: ")
	imapObj.login(USER_EMAIL , USER_PASSWORD)


login_mail_server()

pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['NOT', 'DELETED'])
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])

print message.get_subject()
print message.get_addresses('from')

soup = BeautifulSoup(message.as_string())


