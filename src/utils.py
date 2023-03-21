import os
import sys
import dill
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

        logging.info(f"Object saved at {file_path}")

    except Exception as e:
        logging.error(f"Error in save_object {e}")
        raise CustomException(f"Error in save_object {e}",sys)