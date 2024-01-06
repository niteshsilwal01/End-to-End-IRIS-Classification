from flask import Flask, request, render_template, json
import joblib
import pandas as pd
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/', methods=["GET", "POST"])
def home():
   """
   This is the home page
   ---
   responses:
       200:
           description: Home page
   """
   return render_template("index.html")

@app.route('/predict', methods=["GET", "POST"])
def predict():
  """
  Predict the Iris flower type based on uploaded CSV file
  ---
  parameters:
    - name: file
      in: formData
      type: file
      required: true
      description: The CSV file containing the Iris data
  responses:
      200:
          description: Predicted Iris flower types
          schema:
              type: array
              items:
                 $ref: '#/definitions/Flower'
  definitions:
      Flower:
          type: object
          properties:
              sepal_length:
                 type: number
              sepal_width:
                 type: number
              petal_length:
                 type: number
              petal_width:
                 type: number
              Predicted Flower Type:
                 type: string
  """
  uploaded_file = request.files['file']
  df = pd.read_csv(uploaded_file)
  with open("model.pkl", 'rb') as file:
      classifier = joblib.load(file)
  
  predictions_test = classifier.predict(df)

  df['Predicted Flower Type'] = predictions_test
  return df.to_dict(orient='records')


if __name__ == '__main__':
   app.run(debug=True, port=5002)
