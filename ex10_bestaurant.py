#!/usr/bin/python

import os

total_score = {} 
txts = os.listdir(".")

def parse_file(filename):
	score = {} 
	openfile = open(filename)
	for line in openfile: 
		line = line.split(":")
		score[line[0]] = int(line[1])
	return score

def add_dictionaries(dict1, dict2):
 	for key, value in dict2.items():
 		dict1[key] = dict1.get(key,0) + value

for filename in txts: 
 	if ".txt" in filename:
 		results = parse_file(filename)
 		add_dictionaries(total_score, results)

for key,value in total_score.items():
	print "%s:%s" % (key,value)

# Pseudocode:
#     main loop:
#     create empty total score dictionary
#     get a list of all files in directory
#     for each filename in file list:
#         if filename ends in 'txt':
#             results = parse_file(filename)
#             add_dictionaries(total scores, results)

#     loop through the total score dictionary and print results

#     def parse_file(filename)
#         create an empty score dictionary
#         open the file
#         for each line in the file:
#             split the line by the separator ":"
#             using the first token as a key, insert the second token into the dictionary as a value
#         return the dictionary

#     def add_dictionaries(dict1, dict2):
#         for each key-value pair in dict 2:
#             add the value to the existing value in dict 1


#another way but the files need to be moved to /namestxt/ directory
import os

total_score = {} 
txts = os.listdir("./namestxt/")

for filename in txts:
	openfile = open("./namestxt/" + filename)
	for line in openfile: 
		if line == "":
			break
		else: 
			line = line[0: -1]
			line = line.split(":")
			total_score[line[0]] = total_score.get(line[0],0) + int(line[1])
	openfile.close()

for key in sorted(total_score):
	value = total_score[key]
	print "%s:%s" %(key, value)