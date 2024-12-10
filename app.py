from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load your model and scaler
rf_model = joblib.load('house_price_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load your dataset for stats
data = pd.read_csv('/Users/srisabarish/Downloads/ML_Test/Intern Housing Data India.csv')

# Map ocean_proximity for descriptive stats
ocean_proximity_mapping = {
    'ISLAND': 1,
    'NEAR OCEAN': 2,
    '<1 OCEAN': 3,
    'NEAR BAY': 4,
    'INLAND': 5
}
data['ocean_proximity'] = data['ocean_proximity'].map(ocean_proximity_mapping)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descriptive_stats')
def descriptive_stats():

    stats = data.describe().transpose()

    # Start creating the HTML table for displaying the stats
    table_html = '<table class="table">'
    table_html += '<tr><th>Feature</th><th>Count</th><th>Mean</th><th>Std</th><th>Min</th><th>25%</th><th>50%</th><th>75%</th><th>Max</th></tr>'

    # Loop through the descriptive stats and create rows for the table
    for feature, stats_row in stats.iterrows():
        table_html += f'<tr>'
        table_html += f'<td>{feature}</td>'
        table_html += f'<td>{stats_row["count"]:.0f}</td>'
        table_html += f'<td>{stats_row["mean"]:.2f}</td>'
        table_html += f'<td>{stats_row["std"]:.2f}</td>'
        table_html += f'<td>{stats_row["min"]:.0f}</td>'
        table_html += f'<td>{stats_row["25%"]:.0f}</td>'
        table_html += f'<td>{stats_row["50%"]:.0f}</td>'
        table_html += f'<td>{stats_row["75%"]:.0f}</td>'
        table_html += f'<td>{stats_row["max"]:.0f}</td>'
        table_html += f'</tr>'

    table_html += '</table>'

    # Return the table HTML content
    return table_html


@app.route('/inferential_stats')


def inferential_stats():
    # Example: Correlation matrix
    correlation = data.corr().to_dict()
    return jsonify({'correlation_matrix': correlation})

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the frontend
    data = request.get_json()

    # Extract values from the JSON
    ocean_proximity = data['ocean_proximity']
    total_rooms = data['total_rooms']
    total_bedrooms = data['total_bedrooms']
    median_income = data['median_income']
    median_age = data['median_age']

    # Format the data for prediction
    X = np.array([[ocean_proximity, total_rooms, total_bedrooms, median_income, median_age]])
    X_scaled = scaler.transform(X)

    # Make the prediction
    prediction = rf_model.predict(X_scaled)[0]

    # Return the prediction
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)