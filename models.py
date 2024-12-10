import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib


data = pd.read_csv('/Users/srisabarish/Downloads/ML_Test/Intern Housing Data India.csv')

data.dropna(inplace=True)

ocean_proximity_mapping = {
    'ISLAND': 1,
    'NEAR OCEAN': 2,
    '<1 OCEAN': 3,
    'NEAR BAY': 4,
    'INLAND': 5
}

data['ocean_proximity'] = data['ocean_proximity'].map(ocean_proximity_mapping)

features = ['ocean_proximity', 'total_rooms', 'total_bedrooms', 'median_income', 'housing_median_age']
x = data[features]
y = data['median_house_value']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train) 
x_test_scaled = scaler.transform(x_test)  
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

rf_model.fit(x_train_scaled, y_train)


y_pred = rf_model.predict(x_test_scaled)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R² Score: {r2}")


joblib.dump(rf_model, 'house_price_model.pkl')
print("Model saved as house_price_model.pkl")
joblib.dump(scaler, 'scaler.pkl')
print("Scaler saved as scaler.pkl")
