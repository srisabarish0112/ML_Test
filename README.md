Housing Stats & Prediction
This project provides an interface to view descriptive statistics of housing data and predict house prices based on certain features such as ocean proximity, total rooms, total bedrooms, median income, and median age. It is built using Python (Flask for the backend) and HTML/CSS/JavaScript for the frontend.

Features
Descriptive Stats: View basic statistics of the housing data such as count, mean, standard deviation, and percentiles.
Model Prediction: Input data to predict house prices based on a machine learning model.
User-friendly Interface: The frontend is designed to be clean, responsive, and easy to navigate.
Prerequisites
Python 3.x
Flask
Pandas
Scikit-learn (for machine learning model)
Any modern web browser
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/housing-stats-prediction.git
cd housing-stats-prediction
2. Set up a virtual environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install required dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the application
bash
Copy code
python app.py
The application will run locally on http://127.0.0.1:5000/.

Features
Descriptive Stats
This page displays basic statistics for the housing data, including:
Count
Mean
Standard Deviation (Std)
Minimum (Min)
25th Percentile (25%)
Median (50%)
75th Percentile (75%)
Maximum (Max)
Model Prediction
The user can input the following details for a house:
Ocean Proximity (categorical)
Total Rooms (numeric)
Total Bedrooms (numeric)
Median Income (numeric)
Median Age (numeric)
After entering the data and submitting the form, the app will predict the house price using a machine learning model.
File Structure
bash
Copy code
/housing-stats-prediction
│
├── app.py                # Backend Python code (Flask)
├── requirements.txt      # List of dependencies
├── templates/
│   └── index.html        # Frontend HTML template
└── static/
    └── style.css         # Custom styles for the application
Endpoints
/: The home page of the application.
/descriptive_stats: Displays the descriptive statistics of the housing data.
/predict: Accepts a POST request to predict house prices based on the input data.
Technologies Used
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Machine Learning: Scikit-learn, Pandas
