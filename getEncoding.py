# _*_ encoding: utf-8 _*_
# author: shenpeng
# date: 2015-6-8
# version 1.0

import urllib
import chardet


#In this method, we use chardet library to get the web charset.

def getHtmlEncoding(websize):
	
	data = urllib.urlopen(websize).read()
	return chardet.detect(data)['encoding']

