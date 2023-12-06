import os
import pickle
from sklearn.svm import SVC
from src.utils.common import create_dirs
from sklearn.linear_model import LogisticRegression
from src.logger import logging

class ComponentModelTraining:
    def __init__(self, ModelTrainingEntity)->None:
        self.config = ModelTrainingEntity
        create_dirs([self.config.trained_model_folder])
    
    def _load_svm(self)->None:
        self.svc = SVC(probability=True)
    
    def _save_model(self, model, path)->None:
        with open(path, 'wb') as file:
            pickle.dump(model, file)

    def train_model(self, data:list)->None:
        self._load_svm()
        logging.info("Loaded the sklearn model sucessfully")
        train_df, test_df = data[0], data[1]
        X_train = train_df.iloc[:, 0:-1]
        y_train = train_df.iloc[:,-1]
        X_test = test_df.iloc[:, 0:-1]
        y_test = test_df.iloc[:,-1]
        logging.info("Training started")
        self.svc.fit(X_train, y_train)
        logging.info("Training Completed")
        self._save_model(self.svc, self.config.trained_model_folder)
        logging.info(f"trained model saved to {self.config.trained_model_folder}")