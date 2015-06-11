# _*_ coding: utf-8 _*_
# author: ShenPeng
# date: 2015-06-08
# version: 1.0

#!/usr/bin/python

from email.mime.text import MIMEText
import smtplib

#This moudle is for e-Mail sending.

def makeHtml(filename):
	"""
	In this method, we extract the title and websize from the given file.
	"""

	content = "<h3>北邮计算机学院通知更新：</h3>"
	fileObj = open(filename)
	data = fileObj.read()
	if(len(data) == 0):
		content += "没有任何更新"
	else:
		fileObj.seek(0)
		for eachline in fileObj:
			tmpList = eachline.split(" ")
			content += "<p><a href = %s>%s</a></p>" % (tmpList[0], tmpList[1])
		fileObj.close()

	return content

def sendMail(content):
	"""
	In this method, we use smtplib to send an email.
	You may need to change the related information,
	such as from_addr,password...
	"""
	from_addr = "from@fromdomain.com"	#用户名
	password = "password"	#用户的密码
	to_addr= ["to@todomain.com"]	#收件人
	mailServer = "####"	#设置服务器
	msg = MIMEText(content, "html", "utf-8")
	msg["From"] = "python爱好者 <from@fromdomain.com>"
	msg["To"] = "北邮学子 <to@todomain.com>"
	msg["subject"] = "通知更新"

	try:
		smtpObj = smtplib.SMTP(mailServer)
		smtpObj.set_debuglevel(1)
		smtpObj.login(from_addr, password)
		smtpObj.sendmail(from_addr, to_addr, msg.as_string())
		smtpObj.quit()
	except smtplib.EXCEPTION:
		print "Send mail failure"


#The following was just for testing moudle.
#When you use the main function, you can forget about the following.

if __name__ == "__main__":
	content = makeHtml("differFile.txt")
	print content
	sendMail(content)
