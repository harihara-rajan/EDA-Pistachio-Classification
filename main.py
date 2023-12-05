from src.pipeline.s01_data_ingestion_pipeline import DataIngestionPipeline
from src.logger import logging
logging.info("Welcome to the Pistachio Classification ML Pipeline")
stage01 = "Data Ingestion"

logging.info(f"{stage01} stared")
di = DataIngestionPipeline
di.main()
logging.info(f"{stage01} Ended")


