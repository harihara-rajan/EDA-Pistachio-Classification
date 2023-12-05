from src.config.configuration_manager import ConfigurationManager
from src.components.s01_data_ingestion import ComponentDataIngestion
class DataIngestionPipeline:
    def __init__(self):
        pass
    def main():
        cm = ConfigurationManager()
        data_ingestion_entity = cm.get_data_ingestion_config()
        data_ingestion_component = ComponentDataIngestion(data_ingestion_entity)
        data_ingestion_component.download_data()
        
        
        