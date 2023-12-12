from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

path = "artifacts\data\Pistachio_Dataset\Pistachio_28_Features_Dataset\Pistachio_28_Features_Dataset.xlsx"
features = list(pd.read_excel(path).columns)
features.pop()

@app.route('/')
def Home():
    return render_template('index.html', features=features)

if __name__ == '__main__':
    app.run(debug=True)