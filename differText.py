# _*_ coding: utf-8 _*_
# author: shenpeng
# date: 2015-6-8
# version 1.0

# This moudle is to differ two files, and generate the report.

def simple_differ(presentFile, originalFile, differFile):
	presentFile = open(presentFile)
	originalFile = open(originalFile)
	differFile = open(differFile, "wb")

	firstLine = originalFile.readline()
	for eachline in presentFile:
		if(cmp(eachline, firstLine) != 0):
			differFile.write(eachline)
		else:
			break

	differFile.close()
	presentFile.close()
	originalFile.close()


# test function.
if __name__ == "__main__":
	presentFile = "presentFile.txt"
	originalFile = "originalFile.txt"
	differFile = "differFile.txt"
	simple_differ(presentFile, originalFile, differFile)
