"""
model evaluation components
* include loading the trained model
* evaluating the metrics
    * accuracy 
    * confusion matrix
    * roc curve
"""
import os
import pickle
from src.logger import logging
from src.utils.common import create_dirs, write_yaml
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, RocCurveDisplay, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

class ComponentModelEvaluation:
    def __init__(self,ModelTrainingEntity):
        self.config = ModelTrainingEntity
        self.res_path = os.path.join(os.getcwd(),"artifacts", "Results", "confusion_matrix")
        os.makedirs(self.res_path, exist_ok=True    )
    
    def _load_model(self, model):
        basename = model+"_"+os.path.basename(self.config.trained_model_folder)
        path = os.path.join(os.path.dirname(self.config.trained_model_folder), basename) 
        with open(path, 'rb') as file:
            self.model = pickle.load(file)

    def evaluate(self, test_data):
        modelNames = self.config.name
        scores = []
        plots = []
        for model in modelNames:
            self._load_model(model)
            logging.info(f"Trained {model} Model loaded Sucessfully")
            X_test = test_data[:, 0:-1]
            y_true = test_data[:,-1]
            y_predicted = self.model.predict(X_test)
            y_probs = self.model.predict_proba(X_test)[:,1]

            # auc = roc_auc_score(y_true, y_probs)
            # print(auc)
            # auc_dict = dict(AUC=auc)
            # write_yaml(os.path.join(os.path.dirname(self.res_path), f"auc_{model}.yaml"), auc_dict)
            plt.figure(figsize=(6, 6))
            conf_mat = confusion_matrix(y_true, y_predicted)
            sns.heatmap(conf_mat, annot=True,  fmt="d", cmap="Blues", cbar=False, annot_kws={"size":16})
            plt.xlabel('Predicted Labels')
            plt.ylabel('True Labels')
            plt.title('Confusion Matrix')
            plt.savefig(os.path.join(self.res_path, f'{model}_confusion_matrix.png'), 
                        bbox_inches='tight')

            rep = classification_report(y_true=y_true, y_pred=y_predicted, output_dict=True)
            rep = pd.DataFrame(rep)
            rep.to_csv(os.path.join(self.res_path,f"classification_report_{model}.csv"))

            fpr, tpr, threshold = roc_curve(y_true, y_probs)
            roc_data = dict(falsepr = fpr, truepr = tpr)
            roc_data = pd.DataFrame(roc_data)
            roc_data.to_csv(os.path.join(os.path.dirname(self.res_path),f"roc_{model}.csv"))

            logging.info(f"{model} evaluated on the test dataset sucessfully")
        return None

