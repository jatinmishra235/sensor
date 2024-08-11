import logging, os

log_file = 'logs.log'
logs_dir = os.path.join(os.getcwd(),'logs')
logs_filepath = os.path.join(logs_dir,log_file)
os.makedirs(logs_dir,exist_ok=True)

logging.basicConfig(filename=logs_filepath,level=logging.INFO,format='[%(asctime)s] %(lineno)d %(message)s')

