# Quick Start Guide - Crop Recommendation System

## 🚀 Get Started in 3 Minutes

### Prerequisites
- Python 3.7+ installed
- Internet connection (for pip install)

### Step 1: Install Dependencies (30 seconds)
```bash
pip install -r requirements.txt
```

### Step 2: Train the Model (20 seconds)
```bash
python scripts/train.py
```
You'll see: `Accuracy Score: 0.9932 (99.32%)`

### Step 3: Start the API (5 seconds)
```bash
python app.py
```
You'll see: `Server running at: http://localhost:5000`

### Step 4: Make Your First Prediction

**Using cURL:**
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

**Response:**
```json
{
  "success": true,
  "prediction": {
    "crop": "rice",
    "crop_id": 1,
    "confidence": 99.45
  }
}
```

---

## 📊 What's Included

| File | Purpose |
|------|---------|
| `scripts/train.py` | Train the ML model |
| `scripts/predict.py` | Make predictions programmatically |
| `app.py` | Flask REST API server |
| `test.py` | Automated tests |
| `data/Crop_recommendation.csv` | Training dataset (2200 samples) |
| `models/` | Trained model and scalers (created by train.py) |
| `README.md` | Full documentation |
| `SETUP.md` | Detailed setup guide |

---

## 🌾 Supported Crops (22 Types)

Rice, Maize, Jute, Cotton, Coconut, Papaya, Orange, Apple, Muskmelon, Watermelon, Grapes, Mango, Banana, Pomegranate, Lentil, Blackgram, Mungbean, Mothbeans, Pigeonpeas, Kidneybeans, Chickpea, Coffee

---

## 📡 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | API info |
| `/health` | GET | Health check |
| `/crops` | GET | List crops |
| `/features` | GET | List features |
| `/predict` | POST | Single prediction |
| `/predict-batch` | POST | Multiple predictions |

---

## 💻 Prediction Input Parameters

```json
{
  "N": 90,               // Nitrogen (kg/ha) - 0 to 300
  "P": 42,               // Phosphorus (kg/ha) - 0 to 300
  "K": 43,               // Potassium (kg/ha) - 0 to 300
  "temperature": 20.88,  // Temperature (°C) - 10 to 35
  "humidity": 82.00,     // Humidity (%) - 20 to 100
  "ph": 6.50,            // pH level - 5.0 to 8.0
  "rainfall": 202.94     // Rainfall (mm) - 50 to 500
}
```

---

## 🧪 Testing

Run automated tests:
```bash
python test.py
```

---

## 🔧 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "Model not found" error
```bash
python scripts/train.py
```

### "Port 5000 already in use"
Edit `app.py`, change port from 5000 to 8080:
```python
app.run(host='0.0.0.0', port=8080)
```

---

## 📚 Learn More

- See **README.md** for full documentation
- See **SETUP.md** for detailed setup instructions
- See **scripts/train.py** for model training code
- See **scripts/predict.py** for prediction logic

---

## ✨ Example Use Cases

### Agriculture Planning
"What crops can I grow given my soil conditions?"

### Farm Management
"Is my soil suitable for cotton farming?"

### Educational
"How does ML predict crop recommendations?"

### Research
"What are the key factors for crop selection?"

---

**Ready to start?** Run these three commands:

```bash
pip install -r requirements.txt
python scripts/train.py
python app.py
```

Then visit: **http://localhost:5000**

Happy farming! 🌾
