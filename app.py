from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained KMeans model
model = joblib.load('kmeans_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input from the form (annual income and spending score)
    annual_income = float(request.form['annual_income'])
    spending_score = float(request.form['spending_score'])
    
    # Prepare the input data as a numpy array (matching the input features of the model)
    input_data = np.array([[annual_income, spending_score]])
    
    # Predict the cluster
    cluster = model.predict(input_data)
    
    # Return the result
    return jsonify({'cluster': int(cluster[0])})

if __name__ == '__main__':
    app.run(debug=True)
