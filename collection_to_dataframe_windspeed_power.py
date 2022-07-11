from typing import Mapping, Any
import pandas as pd
from pymongo import collection


def collection_to_dataframe_wind_speed_power(_coll: collection.Collection[Mapping[str, Any]]):
    cursor = _coll.find({}, {'Wind': 1, 'Leistung': 1, '_id': 0})
    _df = pd.DataFrame(list(cursor))
    return _df
