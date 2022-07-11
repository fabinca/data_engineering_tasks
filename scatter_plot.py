from pymongo import MongoClient
from pymongo import collection
from typing import Mapping, Any
import pandas as pd
#import matplotlib.pyplot as plt
import plotly.express as px

PORT = 27017
TURBINES = ["Turbine1", "Turbine2"]


# load wind speed and power to dataframe
def collection_to_dataframe_windspeed_power(_coll: collection.Collection[Mapping[str, Any]]):
    cursor = _coll.find({}, {'Wind': 1, 'Leistung': 1, '_id': 0})
    _df = pd.DataFrame(list(cursor))
    #print(_df)
    return _df


def create_scatter(_dfs, _names):
    for _df in _dfs:
        fig = px.scatter(_df, x="Wind", y="Leistung")
        fig.show()


if __name__ == "__main__":
    client = MongoClient('localhost', PORT)
    db = client["turbines"]
    colls = [db[tur] for tur in TURBINES]
    for coll in colls:
        coll.delete_many({"Dat/Zeit": ""})
    dfs = [collection_to_dataframe_windspeed_power(coll) for coll in colls]
    create_scatter(dfs, TURBINES)
