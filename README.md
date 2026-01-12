# Crop Prediction Using Climate Data 🌾

A machine learning-based crop prediction system that helps farmers determine the most suitable crop to grow based on climate and soil parameters.

## Overview

This project uses climate data (temperature, humidity, rainfall) and soil composition (NPK values, pH) to predict the most suitable crop for cultivation. The system employs a Random Forest classifier to make accurate predictions that can help farmers optimize their crop selection.

## Features

- 🌡️ Predict crops based on temperature, humidity, and rainfall
- 🧪 Consider soil parameters (Nitrogen, Phosphorus, Potassium, pH)
- 🤖 Machine Learning model using Random Forest algorithm
- 💾 Save and load trained models
- 📊 Model evaluation with accuracy metrics
- 🔄 Easy to retrain with new data

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sovan65/Crop-prediction-using-climate-data-.git
cd Crop-prediction-using-climate-data-
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the crop prediction system:
```bash
python crop_prediction.py
```

### Using the CropPredictor Class

```python
from crop_prediction import CropPredictor

# Initialize the predictor
predictor = CropPredictor()

# Load your data
data = predictor.load_data('data/crop_data.csv')

# Prepare and train
X_train, X_test, y_train, y_test = predictor.prepare_data(data)
predictor.train_model(X_train, y_train)

# Evaluate
accuracy = predictor.evaluate_model(X_test, y_test)

# Make predictions
climate_data = {
    'N': 90,
    'P': 42,
    'K': 43,
    'temperature': 20.87,
    'humidity': 82.00,
    'ph': 6.50,
    'rainfall': 202.93
}
predicted_crop = predictor.predict_crop(climate_data)
print(f"Recommended crop: {predicted_crop}")

# Save the model
predictor.save_model('models/crop_predictor.pkl')
```

## Data Format

Your CSV file should contain the following columns:

| Column | Description |
|--------|-------------|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| temperature | Temperature in Celsius |
| humidity | Relative humidity (%) |
| ph | pH value of soil |
| rainfall | Rainfall in mm |
| label | Crop name (target variable) |

Example:
```csv
N,P,K,temperature,humidity,ph,rainfall,label
90,42,43,20.87,82.00,6.50,202.93,rice
85,58,41,21.77,80.31,7.03,226.65,rice
60,55,44,23.00,82.32,7.84,263.96,rice
```

## Project Structure

```
Crop-prediction-using-climate-data-/
│
├── crop_prediction.py      # Main prediction script
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
│
├── data/                   # Data directory
│   ├── README.md          # Data documentation
│   └── crop_data.csv      # Your dataset (add this)
│
└── models/                 # Saved models directory
    └── .gitkeep           # Keeps directory in git
```

## Git Setup Commands

If you're setting up this repository for the first time or connecting to a remote:

```bash
# Navigate to your project directory
cd "path/to/your/crop-prediction"

# Initialize git (if not already initialized)
git init

# Add remote origin
git remote add origin https://github.com/sovan65/Crop-prediction-using-climate-data-.git

# Rename branch to main
git branch -M main

# Add all files
git add .

# Commit changes
git commit -m "Initial commit"

# Push to remote
git push -u origin main
```

## Model Information

- **Algorithm**: Random Forest Classifier
- **Features**: 7 input features (N, P, K, temperature, humidity, pH, rainfall)
- **Preprocessing**: StandardScaler for feature normalization
- **Train/Test Split**: 80/20 ratio

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.

## Acknowledgments

This project aims to help farmers make informed decisions about crop selection based on environmental and soil conditions, potentially improving agricultural productivity and sustainability.
