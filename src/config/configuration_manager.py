from __init__ import PARAMS_PATH, CONFIG_PATH
from src.entity.config_entity import DataIngestionEntity, DataPreprocessEntity
from src.utils.common import read_yaml
class ConfigurationManager:
    def __init__(self, CONFIG_PATH= CONFIG_PATH, PARAMS_PATH= PARAMS_PATH):
        self.config = read_yaml(CONFIG_PATH)
        self.params = read_yaml(PARAMS_PATH)
    
    def get_data_ingestion_config(self)->DataIngestionEntity:
        config = self.config.Data_Ingestion
        data_ingestion_entity = DataIngestionEntity(root_folder = config.root_folder, 
                                                    dataset_name = config.dataset_name)
        return data_ingestion_entity

    def getdata_preprocess_entity(self)->DataPreprocessEntity:
        config = config.Data_Preprocessing
        data_preprocess_entity = DataPreprocessEntity(data_folder=
                                                      config.data_folder)