import sys
import os
from pathlib import Path
from src.utilis.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig
from src.logger import logging
from src.exception import CustomException
import requests
import pandas as pd
from src.constants import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')))

class DataIngestion:
    def __init__(self, )