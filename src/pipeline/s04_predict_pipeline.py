import sys
import pandas as pd 
import pickle


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        model_path = "artifacts/training/SVC_model.pkl"
        preprocess_path = "artifacts/training/SVC_preprocess.pkl"
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        with open(preprocess_path, 'rb') as file:
            preprocessor = pickle.load(file)
        data_scaled = preprocessor.transform(features)
        res = model.predict(data_scaled)
        return res

class CustomData:
    def __init__(self, Area, Perimeter, Major_Axis, Minor_Axis, Eccentricity, Eqdiasq, Solidity, Convex_Area, Extent, Aspect_Ratio, Roundness, Compactness, 
                 Shapefactor_1, Shapefactor_2, Shapefactor_3, Shapefactor_4, Mean_RR, Mean_RG, Mean_RB, StdDev_RR, 
                 StdDev_RG, StdDev_RB, Skew_RR, Skew_RG, Skew_RB, Kurtosis_RR, Kurtosis_RG, 
                 Kurtosis_RB) -> None:
        self.Area = Area
        self.Perimeter = Perimeter
        self.Major_Axis = Major_Axis
        self.Minor_Axis = Minor_Axis
        self.Eccentricity =Eccentricity, 
        self.Eqdiasq = Eqdiasq
        self.Solidity = Solidity
        self.Convex_Area =Convex_Area 
        self.Extent = Extent
        self.Aspect_Ratio = Aspect_Ratio
        self.Roundness = Roundness
        self.Compactness =Compactness
        self.Shapefactor_1 =Shapefactor_1
        self.Shapefactor_2 =Shapefactor_2
        self.Shapefactor_3 =Shapefactor_3
        self.Shapefactor_4 =Shapefactor_4
        self.Mean_RR =Mean_RR
        self.Mean_RG =Mean_RG
        self.Mean_RB =Mean_RB
        self.StdDev_RR = StdDev_RR
        self.StdDev_RG = StdDev_RG
        self.StdDev_RB = StdDev_RB
        self.Skew_RR = Skew_RR
        self.Skew_RG = Skew_RG
        self.Skew_RB = Skew_RB
        self.Kurtosis_RR = Kurtosis_RR
        self.Kurtosis_RG = Kurtosis_RG
        self.Kurtosis_RB = Kurtosis_RB
    def get_data_as_df(self):
        
        datadictionary = dict(
            Area = self.Area,
            Perimeter = self.Perimeter,
            Major_Axis = self.Major_Axis,
            Minor_Axis = self.Minor_Axis,
            Eccentricity =self.Eccentricity, 
            Eqdiasq = self.Eqdiasq,
            Solidity = self.Solidity,
            Convex_Area =self.Convex_Area, 
            Extent = self.Extent,
            Aspect_Ratio = self.Aspect_Ratio,
            Roundness = self.Roundness,
            Compactness =self.Compactness,
            Shapefactor_1 =self.Shapefactor_1,
            Shapefactor_2 =self.Shapefactor_2,
            Shapefactor_3 =self.Shapefactor_3,
            Shapefactor_4 =self.Shapefactor_4,
            Mean_RR =self.Mean_RR,
            Mean_RG =self.Mean_RG,
            Mean_RB =self.Mean_RB,
            StdDev_RR = self.StdDev_RR,
            StdDev_RG = self.StdDev_RG,
            StdDev_RB = self.StdDev_RB,
            Skew_RR = self.Skew_RR,
            Skew_RG = self.Skew_RG,
            Skew_RB = self.Skew_RB,
            Kurtosis_RR = self.Kurtosis_RR,
            Kurtosis_RG = self.Kurtosis_RG,
            Kurtosis_RB = self.Kurtosis_RB)
        return pd.DataFrame(datadictionary)
    
        