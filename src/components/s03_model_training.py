import os
import pickle
from sklearn.svm import SVC
from src.utils.common import create_dirs
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from src.logger import logging

class ComponentModelTraining:
    def __init__(self, ModelTrainingEntity)->None:
        self.config = ModelTrainingEntity
        create_dirs([self.config.trained_model_folder])
    
    def _load_model_for_training(self, name:str)->None:
        if name == "svc" or name == "SVC":
            name_m = "svm"
        
        elif name == "RFC" or name == "RandomForestClassifier" or name == "rfc":
            name_m= "ensemble"
        
        elif name == "LogisticRegression" or name == "LR" or name == "logisticregression":
            name_m = "linear_model"        
        else:
            logging.info("Model not found: %s" % name)
            logging.info("Model Unknown -> choose from SVM, RandomForest or LogisticRegression")
        

        # self.model = SVC(probability=True, C=12, gamma=0.04)    
        # model_class = getattr(__import__(f'sklearn.{name_m}'), name)
        # self.model = model_class()
        module = __import__(f"sklearn.{name_m}", fromlist=[name])
        # Use getattr to get the class from the module
        model_class = getattr(module, name)

        # Create an instance of the model
        self.model = model_class()

    def _save_model(self, model, path)->None:
        model_name = f"{model.__class__.__name__}_{os.path.basename(path)}"
        path = os.path.join(os.path.dirname(path), model_name)
        with open(path, 'wb') as file:
            pickle.dump(model, file)

    
    
    def train_model(self, data:list)->None: # model list [SVC(), LR(), RFC()]
        models = self.config.name
        for modelname in models:
            self._load_model_for_training(modelname)
            logging.info(f"Loaded the sklearn model ({modelname}) sucessfully")
            model_params = self.config.model[modelname] # error here
            self.model.set_params(**model_params)
            train_df, test_df = data[0], data[1]
            X_train = train_df[:, 0:-1]
            y_train = train_df[:,-1]
            X_test = test_df[:, 0:-1]
            y_test = test_df[:,-1]
            logging.info(f"Training {modelname} model started")
            self.model.fit(X_train, y_train)
            logging.info(f"Training {modelname} Completed")
            self._save_model(self.model, self.config.trained_model_folder)
            logging.info(f"trained model saved to {os.path.dirname(self.config.trained_model_folder)}")