import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name="mlproject"
list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init_py__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion",
    f"src/{project_name}/components/data_transformation",
    f"src/{project_name}/components/model_trainier.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/prediction_pipelines.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "dockersfile",
    "requirements.txt",
    "setup.py"

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath,'w') as f:
                pass
                logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} already exists")