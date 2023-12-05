import os 
from pathlib import Path


def create_dirs(abspath:list)-> None:
    """
    This function creates directories 
    args:
    abspath : path for the directory to be created
    """
    for dir in abspath:
        dirname = os.path.dirname(dir)
        os.makedirs(dirname, exist_ok=True)

