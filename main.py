import pprint
from typing import Mapping, Any
import pymongo as pm
from csv import DictReader


def csv_to_mongo(_filename: str, _collection: pm.collection.Collection[Mapping[str, Any]]):
    with open(_filename) as data:
        reader = DictReader(data, delimiter=";")
        header = reader.fieldnames
        for each in reader:
            row = {}
            print(each)
            for field in header:
                row[field] = each[field]
            _collection.insert_one(row)


FILES = ["Turbine1.csv", "Turbine2.csv"]
client = pm.MongoClient()
db = client["test_db"]
collection = db["turbines"]
for file in FILES:
    csv_to_mongo(file, collection)

for info in collection.find({"Rotor": "14,5"}):
    pprint.pprint(info)
