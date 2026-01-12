# Crop Recommendation System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A machine learning-based crop recommendation system that suggests the best crops to cultivate based on soil and environmental parameters.

## 📋 Overview

This project uses a **Random Forest Classifier** to predict the most suitable crop for given soil and environmental conditions. The system analyzes:
- **Soil Nutrients**: Nitrogen (N), Phosphorus (P), Potassium (K)
- **Environmental Factors**: Temperature, Humidity, pH, Rainfall

## 🌾 Supported Crops (22 Types)

1. Rice
2. Maize
3. Jute
4. Cotton
5. Coconut
6. Papaya
7. Orange
8. Apple
9. Muskmelon
10. Watermelon
11. Grapes
12. Mango
13. Banana
14. Pomegranate
15. Lentil
16. Blackgram
17. Mungbean
18. Mothbeans
19. Pigeonpeas
20. Kidneybeans
21. Chickpea
22. Coffee

## 📁 Project Structure

```
crop prediction/
├── data/
│   └── Crop_recommendation.csv        # Dataset with 2200 samples
├── models/
│   ├── crop_recommendation_model.pkl  # Trained Random Forest model
│   ├── minmax_scaler.pkl              # MinMax normalization scaler
│   ├── standard_scaler.pkl            # Standard scaling scaler
│   ├── crop_mapping.pkl               # Crop label mapping
│   └── feature_names.pkl              # Feature names list
├── scripts/
│   ├── train.py                       # Model training script
│   └── predict.py                     # Prediction module
├── app.py                              # Flask REST API
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
python scripts/train.py
```

This will:
- Load the dataset
- Preprocess the data
- Train a Random Forest classifier
- Evaluate the model
- Save the model and scalers to the `models/` directory

**Expected Output:**
```
Accuracy Score: 0.9932 (99.32%)
```

### 3. Test Predictions (Command Line)

```bash
python scripts/predict.py
```

This will run example predictions and show supported crops.

### 4. Run the Web API

```bash
python app.py
```

The API will be available at: **http://localhost:5000**

## 📡 API Endpoints

### 1. Home / API Info
```
GET /
```
Returns API information and available endpoints.

**Response:**
```json
{
  "name": "Crop Recommendation System",
  "version": "1.0.0",
  "endpoints": {...}
}
```

### 2. Health Check
```
GET /health
```
Check if API and model are running.

### 3. Get Supported Crops
```
GET /crops
```
Returns all supported crops with their IDs.

**Response:**
```json
{
  "success": true,
  "total_crops": 22,
  "crops": {
    "rice": 1,
    "maize": 2,
    ...
  }
}
```

### 4. Get Required Features
```
GET /features
```
Returns the list of required input features.

**Response:**
```json
{
  "success": true,
  "features": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
  "feature_count": 7
}
```

### 5. Single Prediction
```
POST /predict
```

**Request Body:**
```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.88,
  "humidity": 82.00,
  "ph": 6.50,
  "rainfall": 202.94
}
```

**Response:**
```json
{
  "success": true,
  "prediction": {
    "crop": "rice",
    "crop_id": 1,
    "confidence": 99.45,
    "input": {...}
  }
}
```

### 6. Batch Predictions
```
POST /predict-batch
```

**Request Body:**
```json
{
  "data": [
    {
      "N": 90,
      "P": 42,
      "K": 43,
      "temperature": 20.88,
      "humidity": 82.00,
      "ph": 6.50,
      "rainfall": 202.94
    },
    {
      "N": 120,
      "P": 70,
      "K": 50,
      "temperature": 28.00,
      "humidity": 65.00,
      "ph": 6.50,
      "rainfall": 200.00
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "total_predictions": 2,
  "predictions": [
    {"crop": "rice", "confidence": 99.45, ...},
    {"crop": "mango", "confidence": 98.12, ...}
  ]
}
```

## 🧪 Example Usage

### Using Python Directly

```python
from scripts.predict import CropRecommendationPredictor

# Initialize predictor
predictor = CropRecommendationPredictor()

# Make a prediction
result = predictor.predict(
    N=90,
    P=42,
    K=43,
    temperature=20.88,
    humidity=82.00,
    ph=6.50,
    rainfall=202.94
)

print(f"Recommended Crop: {result['crop']}")
print(f"Confidence: {result['confidence']}%")
```

### Using cURL

```bash
# Single prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.88,
    "humidity": 82.00,
    "ph": 6.50,
    "rainfall": 202.94
  }'

# Get supported crops
curl http://localhost:5000/crops
```

### Using Python Requests

```python
import requests
import json

# API endpoint
url = "http://localhost:5000/predict"

# Prepare data
data = {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.88,
    "humidity": 82.00,
    "ph": 6.50,
    "rainfall": 202.94
}

# Make request
response = requests.post(url, json=data)
result = response.json()

print(f"Crop: {result['prediction']['crop']}")
print(f"Confidence: {result['prediction']['confidence']}%")
```

## 📊 Model Information

### Algorithm
- **Type**: Random Forest Classifier
- **Number of Trees**: 100
- **Max Depth**: 20
- **Random State**: 42

### Data Preprocessing
1. **Label Encoding**: Crop names mapped to numeric IDs (1-22)
2. **MinMax Scaling**: Features normalized to [0, 1] range
3. **Standard Scaling**: Features standardized (mean=0, std=1)

### Training Data
- **Total Samples**: 2200
- **Training Set**: 1760 (80%)
- **Test Set**: 440 (20%)
- **Features**: 7
- **Classes**: 22

### Model Performance
- **Accuracy**: 99.32%
- **Test Set Size**: 440 samples

## 📈 Feature Importance

The model ranking for feature importance:
1. **Temperature** - Critical for growth
2. **Humidity** - Affects water availability
3. **Rainfall** - Direct water supply
4. **pH** - Soil acidity/alkalinity
5. **Potassium (K)** - Nutrient requirement
6. **Phosphorus (P)** - Nutrient requirement
7. **Nitrogen (N)** - Nutrient requirement

## 🔧 System Requirements

- Python 3.7+
- pip (Python package manager)
- 500MB disk space for models and dependencies

## 📝 Input Parameters Guide

| Parameter | Unit | Range | Description |
|-----------|------|-------|-------------|
| N | kg/ha | 0-300 | Nitrogen content in soil |
| P | kg/ha | 0-300 | Phosphorus content in soil |
| K | kg/ha | 0-300 | Potassium content in soil |
| temperature | °C | 10-35 | Average temperature |
| humidity | % | 20-100 | Relative humidity |
| ph | - | 5.0-8.0 | Soil pH level |
| rainfall | mm | 50-500 | Annual rainfall |

## 🐛 Troubleshooting

### Model Files Not Found
**Error**: "FileNotFoundError: Model not found"
**Solution**: Train the model first using `python scripts/train.py`

### Invalid Input Values
**Error**: "Invalid input value"
**Solution**: Ensure all input values are numeric and within reasonable ranges

### Port Already in Use
**Error**: "Address already in use"
**Solution**: Change port in `app.py` or kill the process using port 5000

## 📚 Dataset Information

The dataset contains 2200 records of soil and climate parameters with corresponding suitable crops. Each record includes:
- Nitrogen, Phosphorus, and Potassium levels
- Temperature and humidity conditions
- Soil pH value
- Annual rainfall
- Actual crop label

## 🎯 Performance Optimization

The model uses:
- **MinMax Scaler**: Normalizes features to [0, 1] range
- **Standard Scaler**: Further standardizes the data
- **Feature Selection**: Uses only 7 most relevant features
- **Random Forest**: Ensemble method for robust predictions

## 🤝 Contributing

To improve the model:
1. Add more training data to `data/Crop_recommendation.csv`
2. Retrain the model: `python scripts/train.py`
3. Test new predictions

## 📄 License

This project is provided as-is for educational and agricultural purposes.

## 👥 Author

Created for crop recommendation and agricultural decision support.

---

**Last Updated**: January 2026

For issues or questions, refer to the project structure and inline documentation in the code.
