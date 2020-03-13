import os
from pulldatamodule import pull_data
from insertdata import insert_data


listOfFiles = os.listdir("/Users/jaroslawkozak/Desktop/betfairmatchoddsdata")
counter = 0

for file in listOfFiles[626:]:
	counter += 1
	matchData = pull_data(file)
	insert_data(matchData)
	print(f"Inserted {counter} of {len(listOfFiles)} to the database")