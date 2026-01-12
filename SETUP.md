# Setup Guide - Crop Recommendation System

## Complete Setup Instructions

Follow these steps to set up and run the Crop Recommendation System on your computer.

## Step 1: System Requirements Check

Before starting, ensure you have:
- **Python 3.7 or higher** installed
- **pip** (Python package manager) installed
- At least **500MB** of free disk space

To check your Python version:
```bash
python --version
```

## Step 2: Install Dependencies

Navigate to the project directory and install all required packages:

```bash
pip install -r requirements.txt
```

This will install:
- pandas: Data manipulation
- numpy: Numerical computing
- scikit-learn: Machine learning
- matplotlib: Data visualization
- seaborn: Statistical visualization
- Flask: Web framework for API
- Flask-CORS: Cross-origin support

## Step 3: Train the Model

Before making predictions, you need to train the model:

```bash
python scripts/train.py
```

**What happens during training:**
1. Loads the dataset (2200 crop records)
2. Preprocesses and encodes the data
3. Splits into training (80%) and testing (20%) sets
4. Applies feature scaling (MinMax + Standard)
5. Trains Random Forest Classifier
6. Evaluates model accuracy
7. Saves model and scalers to `models/` directory

**Expected output:**
```
Accuracy Score: 0.9932 (99.32%)
```

⏱️ **Training time:** ~10-30 seconds (depending on your machine)

### Troubleshooting Training

**Error: "FileNotFoundError: [Errno 2] No such file or directory: '...Crop_recommendation.csv'"**
- Ensure you're in the project root directory
- Check that `data/Crop_recommendation.csv` exists

**Error: "ModuleNotFoundError"**
- Reinstall requirements: `pip install -r requirements.txt`

## Step 4: Test the System

### Option A: Test with Python Script

```bash
python test.py
```

This runs 6 automated tests:
1. Basic single prediction
2. Mango growing conditions
3. Apple growing conditions
4. Batch predictions
5. Crop list retrieval
6. Feature names verification

**Expected output:**
```
✓ PASS: Basic Single Prediction
✓ PASS: Mango Prediction
✓ PASS: Apple Prediction
✓ PASS: Batch Predictions
✓ PASS: Crop List
✓ PASS: Feature Names

All tests passed! ✓
```

### Option B: Manual Test with Prediction Module

```bash
python scripts/predict.py
```

This demonstrates predictions with real examples.

## Step 5: Run the Web API

Start the Flask server:

```bash
python app.py
```

**Expected output:**
```
Crop Recommendation API Server
============================================================
Initializing prediction model...
✓ Model loaded successfully!

Starting Flask server...
Server running at: http://localhost:5000
```

Now you can make requests to the API!

## Step 6: Test the API

### Using a Web Browser

Visit: http://localhost:5000

This shows API information and available endpoints.

### Using Command Line (cURL)

Get supported crops:
```bash
curl http://localhost:5000/crops
```

Make a prediction:
```bash
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
```

### Using Python

```python
import requests

url = "http://localhost:5000/predict"
data = {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.88,
    "humidity": 82.00,
    "ph": 6.50,
    "rainfall": 202.94
}

response = requests.post(url, json=data)
result = response.json()

print(f"Crop: {result['prediction']['crop']}")
print(f"Confidence: {result['prediction']['confidence']}%")
```

## Directory Structure After Setup

```
crop prediction/
├── data/
│   └── Crop_recommendation.csv
├── models/
│   ├── crop_recommendation_model.pkl      ← Created by train.py
│   ├── minmax_scaler.pkl                  ← Created by train.py
│   ├── standard_scaler.pkl                ← Created by train.py
│   ├── crop_mapping.pkl                   ← Created by train.py
│   └── feature_names.pkl                  ← Created by train.py
├── scripts/
│   ├── train.py
│   └── predict.py
├── app.py
├── test.py
├── config.py
├── requirements.txt
├── README.md
├── SETUP.md                               ← This file
└── .gitignore
```

## Common Tasks

### Retrain the Model with New Data

1. Add more records to `data/Crop_recommendation.csv`
2. Run: `python scripts/train.py`

### Change API Port

Edit `app.py` and change:
```python
app.run(
    host='0.0.0.0',
    port=5001,  # Change from 5000 to your desired port
    debug=False
)
```

### Check Model Performance

After training, `train.py` displays:
- Accuracy score
- Classification report (precision, recall, F1-score)
- Feature importance ranking

### Debug API Issues

If the API won't start, check:
1. Is port 5000 available?
   ```bash
   # On Windows, find what's using port 5000
   netstat -ano | findstr :5000
   ```

2. Are all models trained?
   ```bash
   # Check if model files exist
   dir models\
   ```

3. Are dependencies installed?
   ```bash
   pip list | findstr scikit-learn
   ```

## Performance Tips

### For Faster Predictions
- Batch multiple requests using `/predict-batch` endpoint
- The first prediction loads the model (~1 second)
- Subsequent predictions are faster (~10-50ms)

### For Production Use
- Set `API_DEBUG = False` in config
- Run behind a production WSGI server (gunicorn, waitress)
- Use environment variables for configuration
- Add authentication/API keys if needed

## Troubleshooting Checklist

- ✓ Python 3.7+ installed?
- ✓ Dependencies installed via pip?
- ✓ Model trained (models/ directory populated)?
- ✓ Port 5000 not in use?
- ✓ CSV file in correct location?
- ✓ All Python files in correct directories?

## Next Steps

1. **Explore the API**: Try all endpoints listed in README.md
2. **Integrate**: Connect to your application
3. **Expand**: Add more crops or features to the dataset
4. **Deploy**: Use Docker or cloud platforms (AWS, Google Cloud, etc.)

## Support Files

Refer to:
- **README.md**: Detailed project documentation
- **config.py**: Configuration settings
- **scripts/train.py**: Training implementation
- **scripts/predict.py**: Prediction logic
- **app.py**: Flask API implementation

---

**Setup Completed!** Your Crop Recommendation System is ready to use.

Questions? Check the README.md file for detailed API documentation and examples.
