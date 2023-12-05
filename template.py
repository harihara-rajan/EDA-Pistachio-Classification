import os
from pathlib import Path


folder_list =[
    "config.yaml",
    "params.yaml",
    "src/entity/__init__.py",
    "src/config/__init__.py",
    "src/components/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "main.py",
    "dvc.yaml",
]

for foldername in folder_list:
    path_dirname = os.path.dirname(foldername)
    path_base_name = os.path.basename(foldername)
    print(path_dirname, path_base_name)
    os.makedirs(os.path.join(os.getcwd(),path_dirname), exist_ok=True)    
    with open(foldername, 'w') as f:
        pass
        
