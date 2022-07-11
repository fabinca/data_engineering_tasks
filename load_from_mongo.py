import pymongo
from pymongo import MongoClient
from pymongo import collection
from typing import Mapping, Any
import pandas as pd
import matplotlib.pyplot as plt
#import plotly as plt
from datetime import datetime as dt
from . import collection_to_dataframe_windspeed_power

PORT = 27017
TURBINES = ["Turbine1", "Turbine2"]


class MongoPlots:
    def __init__(self, port: int, turbines: list):
        self.port = port
        self.turbines = turbines
        self.client = MongoClient('localhost', self.port)
        self.db = self.client["turbines"]
        for turbine in turbines:
            self.db[turbine].delete_many({"Dat/Zeit": ""})
            self.db[turbine].create_index('Dat/Zeit', unique=True)

    def create_scatter(self, _dfs, _names):
        plot, axs = plt.subplots(len(self.turbines))
        plot.suptitle('Wind speed and Power relation in Turbines')
        i = 0
        for _df in _dfs:
            axs[i].scatter(_df['Wind'], _df['Leistung'], s=1)
            axs[i].set(xlabel='wind speed in m/s', ylabel='power in kW')
            axs[i].set_title(self.turbines[i])
            i += 1
        for ax in axs.flat:
            ax.label_outer()
        return plt.gcf()

    def get_my_fig(self, start, end):
        colls = [self.db[tur] for tur in TURBINES]
        for coll in colls:
            coll.delete_many({"Dat/Zeit": ""})
        dfs = [collection_to_dataframe_windspeed_power(coll) for coll in colls]
        return self.create_scatter(dfs, TURBINES)

    def end_date(self):
        save_last = dt.min()
        for turbine in self.turbines:
            coll = self.db[turbine]
            obj = coll.find().sort({"Dat/Zeit": pymongo.ASCENDING}).limit(1)
            end = obj["Dat/Zeit"]
            if save_last > end:
                end = save_last
        return end

    def start_date(self):
        save_last = dt.max()
        for turbine in self.turbines:
            coll = self.db[turbine]
            obj = coll.find().sort({"Dat/Zeit": pymongo.DESCENDING}).limit(1)
            stat = obj["Dat/Zeit"]
            if save_last < start:
                start = save_last
        return start
