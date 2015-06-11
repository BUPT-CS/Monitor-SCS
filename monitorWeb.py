# _*_ coding: utf-8_*_
# author: shenpeng
# date: 2015-06-08
# version: 1.0

import downloadHtml
import differText
import os
import sendMail


#This is the main moudle.


def isExists(fileName):
	'''
	check the file whether exists
	'''
	return os.path.isfile(fileName)


def monitorHtml(websize, presentFile, originalFile, differFile):

	'''
	monitor assign web, if context of the web has changed then send an email
	'''

	downloadHtml.getList(websize, presentfile)
	if(isExists(originalfile)):
		differText.simple_differ(presentfile, originalfile, differFile)
		content = sendMail.makeHtml(differFile)
		sendMail.sendMail(content)

		#delete originalFile, and change presentFile to originalFile
		os.remove(originalFile)
		os.rename(presentFile,originalFile)

	else:
		content = sendMail.makeHtml(presentFile)
		sendMail.sendMail(content)

		#change presentFile to originalFile
		os.rename(presentFile, originalFile)


if __name__ == '__main__':

	#The websize is scs information websize
	websize = "http://scs.bupt.edu.cn/cs_web/morenews.aspx?colum=%CD%A8%D6%AA%CD%A8%B8%E6"
	presentfile = "presentFile.txt"
	originalfile = 'originalFile.txt'
	differFile = "differFile.txt"
	
	monitorHtml(websize, presentfile, originalfile, differFile)
