from flask import Flask, render_template, request
import pandas as pd
from src.pipeline.s04_predict_pipeline import CustomData, PredictPipeline
app = Flask(__name__)

path = "artifacts\data\Pistachio_Dataset\Pistachio_28_Features_Dataset\Pistachio_28_Features_Dataset.xlsx"
features = list(pd.read_excel(path).columns)
features.pop()

@app.route('/')
def Home():
    return render_template('index.html', features=features)

@app.route('/prediction', methods=['POST'])
def prediction():
    if request.method == 'GET':
        return render_template("index.html", features=features)
    else:
        # we capture the data, perform standard scaling and then predict the datapoint
        data = CustomData(Area = request.form.get('Area'),
            Perimeter = request.form.get('Perimeter'),
            Major_Axis = request.form.get('Major_Axis'),
            Minor_Axis = request.form.get('Minor_Axis'),
            Eccentricity =request.form.get('Eccentricity'), 
            Eqdiasq = request.form.get('Eqdiasq'),
            Solidity = request.form.get('Solidity'),
            Convex_Area =request.form.get('Convex_Area'), 
            Extent = request.form.get('Extent'),
            Aspect_Ratio = request.form.get('Aspect_Ratio'),
            Roundness = request.form.get('Roundness'),
            Compactness =request.form.get('Compactness'),
            Shapefactor_1 =request.form.get('Shapefactor_1'),
            Shapefactor_2 =request.form.get('Shapefactor_2'),
            Shapefactor_3 =request.form.get('Shapefactor_3'),
            Shapefactor_4 =request.form.get('Shapefactor_4'),
            Mean_RR =request.form.get('Mean_RR'),
            Mean_RG =request.form.get('Mean_RG'),
            Mean_RB =request.form.get('Mean_RB'),
            StdDev_RR = request.form.get('StdDev_RR'),
            StdDev_RG = request.form.get('StdDev_RG'),
            StdDev_RB = request.form.get('StdDev_RB'),
            Skew_RR = request.form.get('Skew_RR'),
            Skew_RG = request.form.get('Skew_RG'),
            Skew_RB = request.form.get('Skew_RB'),
            Kurtosis_RR = request.form.get('Kurtosis_RR'),
            Kurtosis_RG = request.form.get('Kurtosis_RG'),
            Kurtosis_RB = request.form.get('Kurtosis_RB')
            )
    
    data_df = data.get_data_as_df()
    pred_pipeline = PredictPipeline()
    res = pred_pipeline.predict(data_df)
    return render_template("res.html", res = res)

if __name__ == '__main__':
    app.run(debug=True)