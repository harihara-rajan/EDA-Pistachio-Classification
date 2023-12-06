from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionEntity:
    root_folder : Path
    dataset_name : str

@dataclass(frozen=True)
class DataPreprocessEntity:
    data_folder: Path

@dataclass(frozen=True)
class ModelTrainingEntity:
    trained_model_folder: Path