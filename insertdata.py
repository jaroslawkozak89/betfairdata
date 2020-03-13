from pymongo import MongoClient

def insert_data(matchData):
	client = MongoClient()

	db = client["matchodds"]
	dbCollection = db["events"]

	eventData = matchData

	if dbCollection.find({"_id" : eventData["_id"]}).count() == 0:

		dbUpload = dbCollection.insert_one(eventData)