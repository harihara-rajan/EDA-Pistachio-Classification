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

def write_yaml(abspath, data:dict):
    """
    this function takes the path, and the data
    to store it as a yaml file in abspath.
    """
    with open(abspath, 'w') as yamlfile:
        yaml.dump(data, yamlfile)

if __name__ == "__main__":
    fname = "params.yaml"
    content = read_yaml(fname)
    print(content)
    content_dict = dict(content.SVC)
    print(f"content: {content.SVC}----{type(content.SVC)}")
    print(f"content_dict: {content_dict}----{type(content_dict)}")
    # for key in content:
    #     print(key)
    #     print(f"type - {type(key)}")
    
    print(content.get("SVC"))