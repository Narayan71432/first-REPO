from pymongo import MongoClient

def get_db_client():
    client = MongoClient("mongodb://localhost:27017/")
    return client['survey_database']

def save_survey_data(db, data):
    collection = db['survey_results']
    collection.insert_one(data)
