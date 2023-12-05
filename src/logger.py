import logging
import os 
# from src.utils.common import create_dir


log_file_dir = "log_dir"
log_file_name = "running_log.log"
log_file_path = os.path.join(os.getcwd(), log_file_dir, log_file_name)
os.makedirs(os.path.dirname(log_file_path), exist_ok=True) # write a function create_dirs in src.utils.common.py and replace this line 

log_format = '[%(asctime)s] : %(levelname)s : %(module)s : %(message)s]' # format

logging.basicConfig(
    filename= log_file_path, 
    level = logging.INFO,
    format= log_format
)

if __name__ == '__main__':
    logging.info("Welcome to the Pistachio Classification ML System")