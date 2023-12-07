import os
import pandas as pd # reading the data
from abc import abstractmethod 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split # train-test split
from sklearn.preprocessing import StandardScaler
### --Req Lib for DataPreprocessing-- ##
from src.entity.config_entity import DataPreprocessEntity
from src.logger import logging
import numpy as np

# preprocess components involve ->loading dataset, scaling the input features, 
# one-hot-encoding of the categorical columns and splitting into train and 
# test set. -> used sklean

class ComponentDataPreprocess:
    def __init__(self, DataPreprocessEntity):
        self.config = DataPreprocessEntity    

    def _read(self):
        # logging.info(f"Reading the data from {self.config.data_folder} stared ")
        self.df = pd.read_excel(self.config.data_folder)
        logging.info(f" Data Reading successfull")

    def _one_hot(self):
        self._read()
        logging.info("OneHot encoding of the categorical feature begins")
        categorical_variable = [cname for cname in self.df.columns if self.df[cname].dtype =="O"]
        label_encoder = LabelEncoder()
        self.df[categorical_variable[0]] = label_encoder.fit_transform(self.df[categorical_variable[0]])
        logging.info("successfully on-hot encoded the categorical features")

    def _data_split(self):
        self._one_hot() # one-hot encoded target variable
        logging.info("train-test split started")

        train, test= train_test_split(self.df, test_size=0.3, shuffle=True, random_state=43) # include this information in params.yaml
        self.data = [train, test]
        logging.info("train-test successfully completed")
        self._scale()

    def _scale(self):
        sc = StandardScaler()
        X_train, X_test = self.data[0].iloc[:,0:-1], self.data[1].iloc[:,0:-1]
        y_train, y_test = self.data[0].iloc[:,-1].values.reshape(-1,1), self.data[1].iloc[:,-1].values.reshape(-1,1)
        
        X_train_scaled = sc.fit_transform(X_train) #numpy array
        X_test_scaled = sc.fit_transform(X_test) # numpy array
        
        X_train_s = np.hstack((X_train_scaled, y_train))
        X_test_s = np.hstack((X_test_scaled, y_test))
        self.data = [X_train_s, X_test_s]

    def preprocess(self):
        # return the train test data after scaling
        self._data_split()
        return self.data


    
