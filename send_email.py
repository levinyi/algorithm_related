import argparse
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
	
def Usage():
    __version__ = "1.0.0"
    print( """
Program: %s
Version: 1.0
Contact: dushiyi@genomics.cn
updated: 
         January 10 2018

Description:
  This script is used for sending emal to users.
 
  If some contents is not correct,please check the script or contact with me.

Usage: python %s [options]
Options:
  -u <str>  your emal account [required].
  -p <str>	your password.
  -s <str>	email subject. default='Result'.
  -t <list>	to whom received the email, may be a list or a str. [required]
  -a <str>	attachment file name. it should be exist.
  -h 		help

Example:
    python %s -u dushiyi@genomics.cn -t dushiyi@genomics.cn -a foo.txt -s nosubject.

"""% (sys.argv[0],sys.argv[0],sys.argv[0]))

def main():
	parser = argparse.ArgumentParser(description= 'this is a script used for send email for users!' )
	parser.add_argument('-u','--youraccount',type=str,required=True,help='it required.')
	parser.add_argument('-s','--subject',type=str,required=False,default='Result',help='it is no required')
	parser.add_argument('-t','--towhom',type=str,required=True,help='its a list like xxx@genomics.cn,xxx@genomics.cn.')
	parser.add_argument('-a','--attachment',type=str,required=False,help='it required.')
	parser.add_argument('-p','--passwords',type=str,required=False,help='it required.')
	parser.add_argument('-c','--content',type=str,required=False,help='it required.')

	args = parser.parse_args()
	if not args.passwords:
		passwords = raw_input("Enter your passwords:")
		# print type(passwords)
	else:
		passwords = args.passwords

	smtp = smtplib.SMTP()
	smtp.connect('smtp.genomics.cn',25)
	smtp.login(args.youraccount,passwords)
	msg = MIMEMultipart()

	msg['Subject'] = Header(args.subject)
	if not args.content:
		content = ("the result is finished!,please check the attachment!")
	else:
		content = args.content
	part = MIMEText(content)
	msg.attach(part)
	### attachment 
	if args.attachment:
		part = MIMEApplication(open(args.attachment,'rb').read())
		part.add_header('Content-Disposition', 'attachment', filename=args.attachment)
		msg.attach(part)
	### sed email
	smtp.sendmail(args.youraccount,args.towhom,msg.as_string())
	smtp.quit()
	print("Successfully sent email")

if __name__ == '__main__':
	main()