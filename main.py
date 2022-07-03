import pprint
from typing import Mapping, Any
import pymongo as pm
from csv import DictReader
from datetime import datetime as dt


def handle_type(_string: str):
    if _string.isdigit():
        #print(type(int(_string)))
        return int(_string)
    try:
        flt = float(_string.replace(",", "."))
        #print(type(flt))
        return flt
    except ValueError: #it's not a float or int - should be datetime
        try:
            time = dt.strptime(_string, '%d.%m.%Y, %H:%M')
            return time
        except ValueError:
            print(f"unexpected format: {_string}")
            return _string





def csv_to_mongo(_filename: str, _collection: pm.collection.Collection[Mapping[str, Any]]):
    with open(_filename) as data:
        reader = DictReader(data, delimiter=";")
        header = reader.fieldnames
        for each in reader:
            row = {}
            for field in header:
                row[field] = handle_type(each[field])
            #print(row)
            _collection.insert_one(row)


FILES = ["Turbine1.csv", "Turbine2.csv"]
client = pm.MongoClient()
db = client["test_db"]
collection = db["turbines"]
for file in FILES:
    csv_to_mongo(file, collection)

if __name__ == "__main__":
    for info in collection.find({"Rotor": 14.5}):
        pprint.pprint(info)

