import sys
import os
from src.utilis.common import read_yaml, create_directories, save_json, load_csv_data
from src.entity.config_entity import ModelEvaluationConfig
from src.logger import logging
from src.exception import CustomException
from src.constants import *
from pathlib import Path
import joblib
from sklearn.metrics import accuracy_score, recall_score, precision_score

class ModelEvaluation:
    def __init__(self, config_path = CONFIG_FILE_PATH):
        self.yaml_content = read_yaml(config_path)
        self.root_dir = Path(__file__).resolve().parents[2]
        self.config = ModelEvaluationConfig(
            
            model_evaluation_path=self.yaml_content['model_evaluation']['model_evaluation_dir'],
            model_path=self.yaml_content['model_evaluation']['model_path'],
            test_data_path=self.yaml_content['model_evaluation']['test_data_path'],
            metric_file_path=self.yaml_content['model_evaluation']['metric_file_path'],
            encoder_path=self.yaml_content['model_evaluation']['encoder_path']
            
        )
        
    def creating_directories(self):
        """Create directories for the model evaluation data, if they do not exist"""
        
        try:
            create_directories(self.root_dir/self.config.model_evaluation_path)
            logging.info(f'Directory created successfully at {self.config.model_evaluation_path}')
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def eval_metircs(self, actual, predict):
        """Evaluation Metircs"""
        
        accuracy = accuracy_score(actual, predict)
        recall = recall_score(actual, predict, average='weighted')
        precision = precision_score(actual, predict, average='weighted')
        
        return accuracy, recall, precision
    
    def load_data(self):
        """Loading the data"""
        
        try:
            logging.info('Loading test data')
            test_data = load_csv_data(Path(self.root_dir/self.config.test_data_path))
            return test_data
        
        except Exception as e:
            logging.error(f'Error occurred: {e}')
            raise CustomException(e,sys)
        
    def model_evaluation(self):
        try:
            self.creating_directories()
            
            test_data = self.load_data()
            logging.info('Test data: {}'.format(test_data))
            
            model = joblib.load(Path(self.root_dir/self.config.model_path))
            encoder = joblib.load(Path(self.root_dir/self.config.encoder_path))
            
            X_test = test_data.drop('prognosis',axis=1)
            y_test = test_data['prognosis']
            
            y_processed_test = encoder.transform(y_test)
            
            y_predict = model.predict(X_test)
            
            accuracy, recall, precision = self.eval_metircs(y_processed_test, y_predict)
            results = {
                'Accuracy': accuracy,
                'Recall': recall,
                'Precision': precision
            }
            
            save_json(Path(self.root_dir/self.config.metric_file_path), results)
            logging.info(f'Results saved at {self.config.metric_file_path}')
            
        except Exception as e:
            logging.error(f'Error occurred: {e}')
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = ModelEvaluation()
    obj.model_evaluation()