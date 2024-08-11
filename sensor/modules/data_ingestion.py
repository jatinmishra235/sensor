from sensor.storage.data import load_dataframe
from sensor.entity.artifact_entity import Data_ingestion_artifact
from sensor.entity.config_entity import Data_ingestion_config
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.constants import *
import sys
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self):
        self.config = Data_ingestion_config()

    def get_dataframe(self):
        try:
            df = load_dataframe(COLLECTION_NAME,DATABASE_NAME)
            logging.info('got dataframe')
            return df
        except Exception as e:
            raise SensorException(e,sys)
        
    def split_data(self,dataframe):
        try:
            train_df,test_df = train_test_split(dataframe)
            train_df.to_csv(self.config.data_ingestion_train_filepath,index=False,header=True)
            test_df.to_csv(self.config.data_ingestion_test_filepath,index=False,header=True)
            logging.info('data split successfully')
        except Exception as e:
            raise SensorException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            df = self.get_dataframe()
            self.split_data(df)
            data_ingestion_artifact = Data_ingestion_artifact(train_filepath=self.config.data_ingestion_train_filepath,
                                                            test_filepath=self.config.data_ingestion_test_filepath)
            logging.info('data ingestion sucessfull')
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)

if __name__ == '__main__':
    di = DataIngestion()
    op=di.initiate_data_ingestion()
    print(op)