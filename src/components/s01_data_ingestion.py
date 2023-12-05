import kaggle
from src.utils.common import create_dirs
from src.logger import logging

class ComponentDataIngestion:
    def __init__(self, DataIngestionEntity):
        self.config = DataIngestionEntity
        create_dirs([self.config.root_folder])
    
    def download_data(self):
        kaggle.api.dataset_download_files(self.config.dataset_name, self.config.root_folder, unzip=True)
        logging.info("Sucessfully downloaded the dataset from kaggle API") 
