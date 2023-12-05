from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionEntity:
    root_folder : Path
    dataset_name : str