#!usr/bin/python

# setup 
ratings = open("scores.txt")

# create dictionary 
restDict = { }

# loop
while True:
	line = ratings.readline()
	if line == "": # the end of the file
		break # break stops LOOP
	else: 
		line = line [0: -1] # remove the last character "\n"
		line = line.split(":") # split the string at : and create a list of all the substring.
		restDict[line[0]] = line[1] # add data to the dictionary (restaurantName, restaurantScore)
						#same as adding items to a list blah[0] = blah1 

# print restDict # regular restDict
for restaurantName in sorted(restDict):
	restaurantScore = restDict[restaurantName] 
	print "%s : %s " %(restaurantName, restaurantScore)
# print sorted(restDict)

ratings.close()
# close file 
