import pandas as pd # reading the data
from abc import abstractmethod 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split # train-test split
### --Req Lib for DataPreprocessing-- ##
from src.entity.config_entity import DataPreprocessEntity

# preprocess components involve ->loading dataset, scaling the input features, 
# one-hot-encoding of the categorical columns and splitting into train and 
# test set. -> used sklean

class ComponentDataPreprocess:
    def __init__(self, DataPreprocessEntity):
        self.config = DataPreprocessEntity
    
    @abstractmethod
    def read(self):
        self.df = pd.read_excel(self.config.data_folder)
    
    @abstractmethod
    def one_hot(self):
        self.read()
        categorical_variable = [cname for cname in self.df.columns if self.df[cname].dtype =="O"]
        label_encoder = LabelEncoder()
        self.df.categorical_variable[0] = label_encoder.fit_transform(self.df.categorical_variable[0])
    
    @abstractmethod
    def data_split(self):
        self.df = self.one_hot() # one-hot encoded target variable
        train_x, test_x, train_y, test_y = train_test_split(self.df, test_size=0.3) # include this information in params.yaml
        self.data = [train_x, train_y, test_x, test_y]

    def preprocess(self):
        # return the train test data after scaling
        self.data_split()
        return self.data


    
