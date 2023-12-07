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
from sklearn.metrics import confusion_matrix, classification_report, RocCurveDisplay, roc_auc_score

class ComponentModelEvaluation:
    def __init__(self,ModelTrainingEntity):
        self.config = ModelTrainingEntity
    
    def _load_model(self):
        with open(self.config.trained_model_folder, 'rb') as file:
            self.model = pickle.load(file)

    def evaluate(self, test_data)->list:
        self._load_model()
        logging.info("Trained Model loaded Sucessfully")
        X_test = test_data[:, 0:-1]
        y_true = test_data[:,-1]
        y_predicted = self.model.predict(X_test)
        y_probs = self.model.predict_proba(X_test)[:,1]

        auc = roc_auc_score(y_true, y_probs)
        conf_mat = confusion_matrix(y_true, y_predicted)
        rep = classification_report(y_true=y_true, y_pred=y_predicted)
        roc_plot = RocCurveDisplay.from_estimator(self.model, X_test, y_true)
        # roc_auc = roc_auc_score(y_true, self.model.predict_proba(X_test),)
        return [conf_mat, rep, roc_plot, auc]
