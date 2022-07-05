import pprint
from typing import Mapping, Any
import pymongo as pm
from csv import DictReader
from datetime import datetime as dt

FILES = ["Turbine1.csv", "Turbine2.csv"]


# otherwise define for each field which type should be used to optimize memory space
def handle_type(_string: str):
    if _string.isdigit():
        return int(_string)
    try:
        flt = float(_string.replace(",", "."))
        return flt
    except ValueError:
        # if it's not a float or int - should be datetime
        try:
            time = dt.strptime(_string, '%d.%m.%Y, %H:%M')
            return time
        except ValueError:
            #print(f"unexpected format: {_string}")
            return _string


def csv_to_mongo_collection(_filename: str, _db):
    coll = _db[_filename.strip(".csv")]
    print(f"Collection {coll} created.")
    with open(_filename) as data:
        reader = DictReader(data, delimiter=";")
        header = reader.fieldnames
        for each in reader:
            row = {}
            for field in header:
                row[field] = handle_type(each[field])
            coll.insert_one(row)
        # delete the second header row
        coll.delete_one({header[0]: ""})
        #print(header[0])
        #resp = coll.create_index(header[0], 1)
        #print(f"Index {header[0]} created. Response: {resp}")



if __name__ == "__main__":
    client = pm.MongoClient()
    db = client["turbines"]
    for file in FILES:
        csv_to_mongo_collection(file, db)
    for collection in db.list_collection_names():
        for info in db[collection].find({"Rotor": 14.5}):
            pprint.pprint(info)
