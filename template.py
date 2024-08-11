import os
from pathlib import Path
from sensor import logger


files = [
    'sensor/__init__.py',
    'sensor/storage/mongodb_connection.py',
    'sensor/constants/__init__.py',
    'sensor/modules/data_ingestion.py',
    'sensor/modules/data_transformation.py',
    'sensor/modules/data_validation.py',
    'sensor/modules/model_trainer.py',
    'sensor/modules/model_evaluation.py',
    'sensor/modules/model_pusher.py',
    'sensor/utils/main_utils.py',
    'sensor/logger.py',
    'sensor/exception.py',
    'sensor/pipeline/training_pipeline.py',
    'sensor/ml/metric.py',
    'sensor/cloud_connection/s3_syncer.py',
    'main.py',
    'setup.py',
    'requirements.txt',
    'config/config.yaml'
]

for file in files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
    else:
        print(f'{filepath}, already exist')

logger.logging.info('done')