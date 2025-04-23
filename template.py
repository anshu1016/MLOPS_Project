import logging
import os
from pathlib import Path

list_of_files = [
".github/workflows/.gitkeep",
"src/init.py",
"src/components/init.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/pipeline/init.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
"src/utils/init.py",
"src/utils/utils.py",
"src/logger/logging.py",
"src/exception/exception.py",
"tests/unit/init.py",
"tests/integration/init.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.ini",
"experiment/experiments.ipynb",
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath) # this will split the tests/unit/__init__.py mean file directory will be tests/unit and file name will be __init__.py
    if filedir != '': # if there is no folder then create here
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # if there is no file then create by checking file is not exists in that folder and also the folder size is zero then only create the file in that particular directory.
        with open(filepath,'w') as f:
            pass # Create an empty file.
    
