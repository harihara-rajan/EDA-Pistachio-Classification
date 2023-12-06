from src.pipeline.s01_data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.s03_model_training_pipeline import ModelTrainingPipeline
from src.pipeline.s02_data_preprocessing_pipeline import DataPreprocessingPipeline
from src.logger import logging
logging.info("Welcome to the Pistachio Classification ML Pipeline")
stage01 = "Data Ingestion"
stage02 = "Data Preprocessing and Model Training"

logging.info(f"{stage01} stared")
di = DataIngestionPipeline
di.main()
logging.info(f"{stage01} Ended")


logging.info(f"{stage02} stared")
di = ModelTrainingPipeline
scores = di.main()
print(scores[0])
logging.info(f"{stage02} Ended")