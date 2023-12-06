"""
model evaluation components
* include loading the trained model
* evaluating the metrics
    * accuracy 
    * confusion matrix
    * roc curve
"""
import pickle
from src.logger import logging
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix

class ComponentModelEvaluation:
    def __init__(self,ModelTrainingEntity):
        self.config = ModelTrainingEntity
    
    def _load_model(self):
        with open(self.config.trained_model_folder, 'rb') as file:
            self.model = pickle.load(file)

    def evaluate(self, test_data)->list:
        self._load_model()
        logging.info("Trained Model loaded Sucessfully")
        X_test = test_data.iloc[:, 0:-1]
        y_true = test_data.iloc[:,-1]
        y_predicted = self.model.predict(X_test)
        print(type(y_predicted))
        conf_mat = confusion_matrix(y_true, y_predicted)
        # roc_auc = roc_auc_score(y_true, self.model.predict_proba(X_test),)
        return [conf_mat]
