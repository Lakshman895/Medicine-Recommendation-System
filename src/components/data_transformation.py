import sys
import os
from src.logger import logging
from src.exception import CustomException
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')))
from src.utilis.common import read_yaml, create_directories, load_csv_data,save_json
from src.entity.config_entity import DataTransformationConfig
from pathlib import Path
from sklearn.model_selection import train_test_split
from src.constants import *

class DataTransformation():
    def __init__(self, config_path=CONFIG_FILE_PATH):
        logging.info('Entered Data Transformation')
        self.yaml_content = read_yaml(config_path)
        self.root_dir = Path(__file__).resolve().parents[2]
        self.config = DataTransformationConfig(
            
            root_dir=self.yaml_content['data_transformation']['root_dir'],
            symptoms_list_path=self.yaml_content['data_transformation']['symptoms_list_path']
            
        )
        
    def creating_directories(self):
        """Create directories for the data transformation data, if they do not exist"""
        
        try:
            create_directories(self.root_dir/self.config.root_dir)
            logging.info(f'Directory created successfully at {self.config.root_dir}')
            
            create_directories(self.root_dir/self.config.symptoms_list_path)
            logging.info(f'Directory created successfully at {self.config.symptoms_list_path}')
            
        except Exception as e:
            logging.error(f'Failed to create directory at {self.data_transformation_path}: {e}')
            raise CustomException(e,sys)
        
    def creating_symptoms_list(self, columns):
        """Creating the list of columns in json file to get the list of symptoms"""
        
        try:
            symptoms_dict = {}
            for i,col in enumerate(columns):
                if col=='prognosis':
                    continue
                col = col.replace('_','')
                symptoms_dict[col] = i
            save_json(Path(self.root_dir/self.config.symptoms_list_path/'symptoms.json'), symptoms_dict)
            logging.info(f'Saved the symptoms json successfully as {self.config.symptoms_list_path}')
            
        except Exception as e:
            logging.error(f'Error occurred: {e}')
            raise CustomException(e,sys)
        
    def data_transformation(self):
        """Splitting the training data and testing data """
        self.creating_directories()
        
        try:
            data_path = self.root_dir/'artifacts/data_ingestion/training.csv'
            data = load_csv_data(Path(data_path))
            logging.info(f'Loaded training data successfully \n {data.head()}')
            
            self.creating_symptoms_list(data.columns)
            
            train_data,test_data = train_test_split(data,test_size=0.2,random_state=42)
            
            train_data.to_csv(Path(self.root_dir/self.config.root_dir)/'train.csv', index=False)
            logging.info(f'Saved the training data successfully as {self.config.root_dir}/train.csv')
            
            test_data.to_csv(Path(self.root_dir/self.config.root_dir)/'test.csv', index=False)
            logging.info(f'Saved the testing data successfully as {self.config.root_dir}/test.csv')
            
        except Exception as e:
            logging.error(f'Error occurred during data transformation: {e}')
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataTransformation()
    obj.data_transformation()