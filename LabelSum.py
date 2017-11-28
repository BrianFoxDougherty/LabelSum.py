import argparse
import sys
import json
from pprint import pprint

"""

LabelSum.py

Author: Brian Fox Dougherty

Operation: Given a JSON string which describes a menu, calculate the SUM of the IDs of all "items", as long as a "label" exists for that item.

"""


debug = 0 # default debug value.  if set to 1 we will output operation information
jsonFile = "" # location of json file to parse

print(" ")
print("------------------------------------------------------------------")
print("This program uses a command line arg -f to point to a JSON file and will sum up all IDs for an item with a label")
print("You also may use the argument -d to turn on debug output.")
print("That contains the string 'label'.")
print(" ")
print("Example without debugging:")
print("LabelSum.py \"c:\\temp\\Data.json\"")
print(" ")
print("Example with debugging:")
print("LabelSum.py \"c:\\temp\\Data.json\" -d")
print("------------------------------------------------------------------")
print(" ")

# create argument parser to get file path and debug var
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument("--filepath", "-f", help="set path to json file")
parser.add_argument("--debug", "-d", help="turn on debug output", action='store_true')

# read arguments 
args = parser.parse_args()

# check for filepath and add it
if args.filepath:  
    jsonFile =  args.filepath

# check for debug and turn on
if args.debug:  
    debug = 1


if debug == 1:
	print("Importing from file: ", jsonFile)

with open(jsonFile, "r") as source:
    jsonSource = source.read()
    data = json.loads('[{}]'.format(jsonSource)) # load and add bracket to each json object

if debug == 1:
	print("JSON data imported:")
	pprint(data)  #output all data elements

print("Output: ")
print(" ")

for i in data:
	IdSum = 0 # reset the sum of IDs for every loop
	
	MenuList = i["menu"] # drop each json object into a list
	
	ItemDict = (MenuList["items"]) # put each list value into a dict
	
	for index, item in enumerate(ItemDict):  # walk through the values in each dict
		if str(item) != "None": # exclude null values which are represented as None
			if 'label' in item:  # label exists, sum the ids
				IdSum = IdSum + item["id"]
				if debug == 1:
					print("Adding item id: ", item["id"])
			else: 
				if debug == 1:
					print("No label for id ", item["id"])

	print(IdSum) # print the final sum for each item

print(" ")
print("Finished!")
