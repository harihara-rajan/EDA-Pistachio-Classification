import os 
import yaml 
from pathlib import Path
from box import ConfigBox
from src.logger import logging

def read_yaml(path:Path)->ConfigBox:
    """
    This function reads the yaml file and 
    returns the content as a ConfigBox object
    args:
    path: Path to the yaml file
    returns: ConfigBox object with yaml content
    """
    with open(path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file {os.path.basename(path)} \
read sucessfully")
    return ConfigBox(content)

def create_dirs(abspath:list)-> None:
    """
    This function creates directories 
    args:
    abspath : path for the directory to be created
    """
    for dir in abspath:
        dirname = os.path.dirname(dir)
        os.makedirs(dirname, exist_ok=True)
    logging.info(f"Created directory {dirname} suceessfully")