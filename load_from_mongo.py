from pymongo import MongoClient
from pymongo import collection
from typing import Mapping, Any
import pandas as pd
import matplotlib.pyplot as plt

PORT = 27017


# load wind speed and power to dataframe
def collection_to_dataframe_windspeed_power(_coll: collection.Collection[Mapping[str, Any]]):
    cursor = _coll.find({}, {'Wind': 1, 'Leistung': 1, '_id': 0})
    _df = pd.DataFrame(list(cursor))
    #print(_df)
    return _df


def create_scatter(_df: pd.DataFrame):
    plt.scatter(df['Wind'], df['Leistung'])
    plt.show()




#create scatterplot

if __name__ == "__main__":
    client = MongoClient('localhost', PORT)
    db = client["turbines"]
    collection = db["Turbine1"]
    collection.delete_many({"Dat/Zeit": ""})
    df = collection_to_dataframe_windspeed_power(collection)
    create_scatter(df)
    print(df)