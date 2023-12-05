import os
import kaggle
from pathlib import Path
def download(copy_from_url:str, path:Path)->None:
    os.makedirs(path, exist_ok=True)
    kaggle.api.dataset_download_files(copy_from_url, path, unzip=True)
