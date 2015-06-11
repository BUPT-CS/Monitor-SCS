# _*_ coding: utf-8 _*_
# author: shenpeng
# date: 2015-6-8
# version 1.0

import urllib
import getEncoding
import sys
import re

#This moudle is to download Html, and get the information.

def donwloadHtml(websize):

	encoding = getEncoding.getHtmlEncoding(websize)
	content = urllib.urlopen(websize).read()
	syscoding = sys.getfilesystemencoding()
	html = content.decode(encoding, "ignore").encode(syscoding)
	
	return html

def getList(websize, savefile):

	html = donwloadHtml(websize)
	file = open(savefile, "wb")
	m = re.findall('<a href="(s\S+)".+>+(.+)<',html)
	for i in m:
		tmp = len(i)
		#Total 2 separate information, one for websize, anoter for title.
		for j in  i:
			if(tmp>1):
				#Add prefix
				file.write("http://scs.bupt.edu.cn/cs_web/"+j+' ')
				tmp = tmp-1
			else:
				file.write(j+'\n')
	file.close()


# test function.
if __name__ == '__main__':
	websize = "http://scs.bupt.edu.cn/cs_web/morenews.aspx?colum=%CD%A8%D6%AA%CD%A8%B8%E6"
 	filename = "originalFile.txt"
 	getList(websize, filename)
