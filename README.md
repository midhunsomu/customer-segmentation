
# Customer Segmentation using KMeans Clustering

## Description
This project implements a **Customer Segmentation** web application using the **KMeans Clustering** algorithm to categorize customers based on their **Annual Income** and **Spending Score**. The application allows users to input customer data via a simple web interface and predict the customer’s cluster using a pre-trained KMeans model. This project showcases how to deploy machine learning models into production with a user-friendly web interface.

## Features
- **User Input:** Collects customer data (Annual Income and Spending Score) from a simple form.
- **Prediction:** Uses a pre-trained **KMeans clustering model** to predict the customer’s cluster based on input data.
- **Web Interface:** Built with **Flask** for an interactive and responsive user experience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/midhunsomu/customer-segmentation.git
   ```

2. Navigate to the project directory:
   ```bash
   cd customer-segmentation
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make sure to have the pre-trained **KMeans model** (`kmeans_model.pkl`) available in the project directory. You can either train the model or load your existing model into the project.

## Usage

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Open a browser and visit `http://127.0.0.1:5000/` to interact with the web interface.

3. Fill in the form with **Annual Income** and **Spending Score** and click **Predict Cluster**.

4. The application will return the predicted customer cluster (e.g., Cluster 1, Cluster 2, etc.).

## Files
- **app.py**: Main Flask application file.
- **index.html**: HTML form for collecting user input and displaying results.
- **kmeans_model.pkl**: Pre-trained KMeans model file used for clustering.

## Technologies Used
- **Python**: Main programming language.
- **Flask**: Framework used for building the web application.
- **KMeans**: Machine learning algorithm used for clustering.
- **joblib**: For loading the pre-trained KMeans model.
- **HTML & JavaScript**: For building the front-end user interface.

## Model Training
- **KMeans Clustering** is used to categorize customers based on their annual income and spending score. The model was trained on historical customer data and saved as `kmeans_model.pkl`.

## Example

1. After running the application, enter the **Annual Income** and **Spending Score** in the form.
2. The model will predict the customer’s cluster and display it on the webpage.

### Example Input:
- **Annual Income**: 50000
- **Spending Score**: 60

### Example Output:
- **Predicted Cluster**: Cluster 2


---
