import pymongo
from pymongo import MongoClient
from pymongo import collection
import pymongo
import pymongo as pm
from typing import Mapping, Any
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

PORT = 27017
TURBINES = ["Turbine1", "Turbine2"]
client = MongoClient('localhost', PORT)
db = client["turbines"]


# load wind speed and power to dataframe
def collection_to_dataframe_windspeed_power(_coll: collection.Collection[Mapping[str, Any]], start, end):
    time_range = {"Dat/Zeit": {"$gte": start, "$lte": end}}
    cursor = _coll.find(time_range, {'Wind': 1, 'Leistung': 1, '_id': 0})
    _df = pd.DataFrame(list(cursor))
    #print(_df)
    return _df


def create_scatter(_dfs, _names):
    plot, axs = plt.subplots(len(TURBINES))
    plot.suptitle('Wind speed and Power relation in Turbines')
    i = 0
    for _df in _dfs:
        axs[i].scatter(_df['Wind'], _df['Leistung'], s=1)
        axs[i].set(xlabel='wind speed in m/s', ylabel='power in kW')
        axs[i].set_title(TURBINES[i])
        i += 1
    for ax in axs.flat:
        ax.label_outer()
    #plt.show()
    return plt.gcf()


def get_my_fig(start, end):
    colls = [db[tur] for tur in TURBINES]
    for coll in colls:
        coll.delete_many({"Dat/Zeit": ""})
    try:
        start = datetime.strptime(start, '%Y%m%d %H:%M')
    except ValueError:
        start = datetime.strptime("1900", '%Y')
    try:
        end = datetime.strptime(end, '%Y%m%d %H:%M')
    except ValueError:
        end = datetime.strptime("2050", '%Y')
    dfs = [collection_to_dataframe_windspeed_power(coll, start, end) for coll in colls]
    create_scatter(dfs, TURBINES)
    return plt.gcf()

"""
def end_date():
    end = datetime.strptime("2050", '%Y')
    for turbine in TURBINES:
        coll = db[turbine]
        obj = coll.find().sort({"Dat/Zeit": pymongo.ASCENDING}).limit(1)
        save_last = obj["Dat/Zeit"]
        if save_last < end:
            end = save_last
    return end


def start_date():
    _start = datetime.strptime("1900", '%Y')
    for turbine in TURBINES:
        coll = db[turbine]
        obj = coll.find().sort({"Dat/Zeit": pymongo.DESCENDING}).limit(1)
        save_last = obj["Dat/Zeit"]
        if save_last > _start:
            _start = save_last
    return _start
"""

if __name__ == "__main__":
    get_my_fig(False, False)
