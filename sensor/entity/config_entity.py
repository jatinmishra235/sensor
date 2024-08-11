from datetime import datetime
import os
from sensor.constants import ARTIFACT_DIR
from dataclasses import dataclass
from sensor.constants import *

timestamp=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
@dataclass
class Training_config:
    artifact_dir = os.path.join(ARTIFACT_DIR,timestamp)

@dataclass
class Data_ingestion_config:
    data_ingestion_dir = os.path.join(Training_config.artifact_dir,DATA_INGESTION_DIR)
    os.makedirs(data_ingestion_dir,exist_ok=True)
    data_ingestion_train_filepath = os.path.join(data_ingestion_dir,TRAIN_FILE)
    data_ingestion_test_filepath = os.path.join(data_ingestion_dir,TEST_FILE)




