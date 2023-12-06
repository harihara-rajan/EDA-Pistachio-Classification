from src.config.configuration_manager import ConfigurationManager
from src.components.s02_data_preprocessing_component import ComponentDataPreprocess
class DataPreprocessingPipeline:
    def __init__(self):
        pass

    def main():
        cm = ConfigurationManager()
        data_preprocess_entity = cm.getdata_preprocess_entity()
        components_preprocess = ComponentDataPreprocess(data_preprocess_entity)
        components_preprocess.preprocess()