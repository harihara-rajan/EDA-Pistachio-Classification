import logging
import os 
import sys


log_file_dir = "log_dir"
log_file_name = "running_log.log"
log_file_path = os.path.join(os.getcwd(), log_file_dir, log_file_name)
# creating the directory for logfile if it doesn't exist
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
with open(log_file_path, 'w') as f:
    pass

log_format = '[%(asctime)s] : %(levelname)s : %(module)s : %(message)s]' # format

logging.basicConfig(
    level = logging.INFO,
    format= log_format, 
    handlers=[
        logging.FileHandler(log_file_path), 
        logging.StreamHandler(sys.stdout)
    ]
)
