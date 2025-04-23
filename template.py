import logging
import os
from pathlib import Path

# list_of_files = [
# ".github/workflows/.gitkeep",
# "src/init.py",
# "src/components/init.py",
# "src/components/data_ingestion.py",
# "src/components/data_transformation.py",
# "src/components/model_trainer.py",
# "src/components/model_evaluation.py",
# "src/pipeline/init.py",
# "src/pipeline/training_pipeline.py",
# "src/pipeline/prediction_pipeline.py",
# "src/utils/init.py",
# "src/utils/utils.py",
# "src/logger/logging.py",
# "src/exception/exception.py",
# "tests/unit/init.py",
# "tests/integration/init.py",
# "init_setup.sh",
# "requirements.txt",
# "requirements_dev.txt",
# "setup.py",
# "setup.cfg",
# "pyproject.toml",
# "tox.ini",
# "experiment/experiments.ipynb",
# ]



# for filepath in list_of_files:
#     filepath = Path(filepath)
#     filedir,filename = os.path.split(filepath) # this will split the tests/unit/__init__.py mean file directory will be tests/unit and file name will be __init__.py
#     if filedir != '': # if there is no folder then create here
#         os.makedirs(filedir,exist_ok=True)
#         logging.info(f"creating directory: {filedir} for file : {filename}")

#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # if there is no file then create by checking file is not exists in that folder and also the folder size is zero then only create the file in that particular directory.
#         with open(filepath,'w') as f:
#             pass # Create an empty file.
    

# delete the path now
# This is the code to delete the files.


# for filepath in list_of_files:
#     path = Path(filepath)
#     if path.exists() and path.is_file(): # checks if the file exists and it's a file.
#         path.unlink() # deletes the file
#         print(f"Deleted file: {filepath}")
    
#     directories = sorted({Path(f).parent for f in list_of_files},key=lambda x: -len(x.parts))
    
#     """ 
#     {Path(f).parent for f in list_of_files}: Creates a set of directories that contain the files.
#         and
#     .parent gives you the folder of each file (e.g., "src/components" for "src/components/init.py").

#     # sorted(..., key=lambda x: -len(x.parts)):
#     Sorts the directories from deepest (longest path) to shallowest.
#     # Example:
#     src/components       (3 parts)
#     src/components/data  (4 parts)
#     We sort in reverse so we delete inner folders first. This avoids trying to delete a parent folder that still has content in it.

#     """
#     for directory in directories:
#         if directory.exists() and not any (directory.iterdir()):
#             directory.rmdir() # remove or delete the directory or folder
#             print(f"Deleted empty directory: {directory}")

#             """
#             directory.exists(): Checks if the folder still exists.

#             directory.iterdir(): Lists the contents inside the folder.

#             not any(...): Ensures the folder is empty.

#             directory.rmdir(): Deletes the directory only if it's empty.
#             """


# we are again creating new list of files for creating Python Package from scratch.

package_name = 'mongodb_connect'

list_of_files = [
    
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "init_setup.sh",
   "requirements.txt", 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb",                     
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