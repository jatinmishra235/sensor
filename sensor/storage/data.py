import pandas as pd
from sensor.constants import DATABASE_NAME,COLLECTION_NAME
from sensor.storage.mongodb_connection import Mongodb
from sensor.logger import logging
import numpy as np


def save_csv(filepath,collection_name,database_name):
    mongodb = Mongodb(collection_name,database_name)
    db = mongodb.database
    if collection_name in db.list_collection_names():
        logging.info('collection already present')
    else:
        collection = mongodb.collection
        df = pd.read_csv(filepath)
        collection.insert_many(df.to_dict('records'))
        logging.info('data uploaded to mongodb sucessfullly')


def load_dataframe(collection_name,database_name):
    mongodb = Mongodb(collection_name, database_name)
    collection = mongodb.collection
    df = pd.DataFrame(list(collection.find()))
    if '_id' in df.columns:
        df = df.drop('_id',axis=1)
    df = df.replace('na',np.nan)
    return df


# save_csv('aps_failure_set.csv','sensor','practice')

