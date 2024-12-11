import unittest
import json
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    def test_descriptive_stats(self):
        # Test the descriptive_stats route
        response = self.app.get('/descriptive_stats')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<table', response.data)
        self.assertIn(b'<th>Feature</th>', response.data)

    def test_predict(self):
        # Test the predict route with sample input
        sample_input = {
            "ocean_proximity": 3,
            "total_rooms": 5000,
            "total_bedrooms": 1000,
            "median_income": 5.5,
            "median_age": 30
        }
        response = self.app.post('/predict', 
                                 data=json.dumps(sample_input),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('prediction', response_data)
        self.assertIsInstance(response_data['prediction'], float)

if __name__ == '__main__':
    unittest.main()