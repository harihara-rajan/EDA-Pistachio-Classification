from src.config.configuration_manager import ConfigurationManager
from src.components.s02_data_preprocessing_component import ComponentDataPreprocess
from src.components.s03_model_training import ComponentModelTraining
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main():
        cm = ConfigurationManager()

        preprocess_config = cm.getdata_preprocess_entity()
        preprocess_component =ComponentDataPreprocess(preprocess_config)
        data = preprocess_component.preprocess()
        
        model_training_config = cm.get_trained_model_config()
        training_components = ComponentModelTraining(model_training_config)
        training_components.train_model(data)