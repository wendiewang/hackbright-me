#!usr/bin/python

import os, shutil 

# chk if directory exists, if not, make directory
if not os.path.exists("sorted"):
	os.mkdir("sorted")

# change into directory
os.chdir("sorted")

# http://stackoverflow.com/questions/3190122/python-how-to-print-range-a-z
for i in range(ord('a'), ord('z')+1):
	if not os.path.exists(chr(i)):
		os.mkdir(chr(i))
		print chr(i),

# http://stackoverflow.com/questions/120656/directory-listing-in-python
for dirname, dirnames, filenames in os.walk('/home/wendy/Documents/files'):
    for filename in filenames:
        print os.path.join(dirname, filename)
	# print only the first letter [0] in filename 
	print filename[0] 
	
	shutil.move(os.path.join(dirname, filename), filename[0])
# shutil.move([from]/home/wendy/documents/files/aexwin.txt, [to] a) 

