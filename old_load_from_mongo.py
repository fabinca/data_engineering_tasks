from pymongo import MongoClient
from pymongo import collection
from typing import Mapping, Any
import pandas as pd
import matplotlib.pyplot as plt
#import plotly as plt

PORT = 27017
TURBINES = ["Turbine1", "Turbine2"]


# load wind speed and power to dataframe
def collection_to_dataframe_windspeed_power(_coll: collection.Collection[Mapping[str, Any]]):
    cursor = _coll.find({}, {'Wind': 1, 'Leistung': 1, '_id': 0})
    _df = pd.DataFrame(list(cursor))
    #print(_df)
    return _df


def create_scatter(_dfs, _names):
    plot, axs = plt.subplots(len(TURBINES))
    plot.suptitle('Horizontally stacked subplots')
    i = 0
    for _df in _dfs:
        axs[i].scatter(_df['Wind'], _df['Leistung'], s=1)
        axs[i].set(xlabel='wind speed in m/s', ylabel='power in kW')
        axs[i].set_title(TURBINES[i])
        i += 1
    #plt.xlabel("wind speed in m/s")
    #plt.ylabel("power in kW")
    #plt.title("Wind speed and Power relation in Turbines")
    #plt.legend(_names)


def get_my_fig(start, end):
    client = MongoClient('localhost', PORT)
    db = client["turbines"]
    colls = [db[tur] for tur in TURBINES]
    for coll in colls:
        coll.delete_many({"Dat/Zeit": ""})
    dfs = [collection_to_dataframe_windspeed_power(coll) for coll in colls]
    create_scatter(dfs, TURBINES)
    return plt.gcf()
