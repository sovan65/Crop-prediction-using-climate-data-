"""
Flask REST API for Crop Recommendation System

This API provides endpoints for making crop recommendations based on soil
and environmental conditions.
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import sys
import traceback

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from predict import CropRecommendationPredictor

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize predictor globally
predictor = None

def initialize_predictor():
    """Initialize the predictor."""
    global predictor
    try:
        predictor = CropRecommendationPredictor()
        return True
    except Exception as e:
        print(f"Error initializing predictor: {e}")
        return False

@app.before_request
def before_request():
    """Ensure predictor is initialized."""
    global predictor
    if predictor is None:
        if not initialize_predictor():
            return jsonify({
                'success': False,
                'error': 'Failed to initialize prediction model'
            }), 500

@app.route('/', methods=['GET'])
def home():
    """Serve the web interface."""
    try:
        return send_file('index.html')
    except:
        # Fallback to API info if HTML not found
        return jsonify({
            'name': 'Crop Recommendation System',
            'version': '1.0.0',
            'description': 'ML-based crop recommendation API using Random Forest',
            'endpoints': {
                'GET /': 'This page',
                'POST /predict': 'Make a single prediction',
                'POST /predict-batch': 'Make multiple predictions',
                'GET /crops': 'List all supported crops',
                'GET /features': 'List required input features',
                'GET /health': 'Check API health'
            }
        }), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    global predictor
    return jsonify({
        'status': 'healthy',
        'model_loaded': predictor is not None
    }), 200

@app.route('/crops', methods=['GET'])
def get_crops():
    """Get list of all supported crops."""
    global predictor
    
    if predictor is None:
        return jsonify({
            'success': False,
            'error': 'Model not initialized'
        }), 500
    
    try:
        crops = predictor.get_crop_info()
        # Sort by ID
        sorted_crops = dict(sorted(crops.items(), key=lambda x: x[1]))
        return jsonify({
            'success': True,
            'total_crops': len(sorted_crops),
            'crops': sorted_crops
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/features', methods=['GET'])
def get_features():
    """Get required input features for prediction."""
    global predictor
    
    if predictor is None:
        return jsonify({
            'success': False,
            'error': 'Model not initialized'
        }), 500
    
    try:
        features = predictor.get_feature_names()
        return jsonify({
            'success': True,
            'features': features,
            'feature_count': len(features)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/predict', methods=['POST'])
def predict():
    """
    Make a crop recommendation prediction.
    
    Expected JSON:
    {
        "N": <float>,           # Nitrogen (kg/ha)
        "P": <float>,           # Phosphorus (kg/ha)
        "K": <float>,           # Potassium (kg/ha)
        "temperature": <float>, # Temperature (°C)
        "humidity": <float>,    # Humidity (%)
        "ph": <float>,          # pH level
        "rainfall": <float>     # Rainfall (mm)
    }
    """
    global predictor
    
    if predictor is None:
        return jsonify({
            'success': False,
            'error': 'Model not initialized'
        }), 500
    
    try:
        # Get JSON data
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'error': f'Missing required fields: {", ".join(missing_fields)}',
                'required_fields': required_fields
            }), 400
        
        # Make prediction
        result = predictor.predict(
            N=float(data['N']),
            P=float(data['P']),
            K=float(data['K']),
            temperature=float(data['temperature']),
            humidity=float(data['humidity']),
            ph=float(data['ph']),
            rainfall=float(data['rainfall'])
        )
        
        return jsonify({
            'success': True,
            'prediction': result
        }), 200
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': f'Invalid input value: {str(e)}'
        }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Prediction error: {str(e)}',
            'traceback': traceback.format_exc()
        }), 500

@app.route('/predict-batch', methods=['POST'])
def predict_batch():
    """
    Make batch predictions for multiple soil/environment conditions.
    
    Expected JSON:
    {
        "data": [
            {
                "N": <float>,
                "P": <float>,
                "K": <float>,
                "temperature": <float>,
                "humidity": <float>,
                "ph": <float>,
                "rainfall": <float>
            },
            ...
        ]
    }
    """
    global predictor
    
    if predictor is None:
        return jsonify({
            'success': False,
            'error': 'Model not initialized'
        }), 500
    
    try:
        # Get JSON data
        request_data = request.get_json()
        
        if 'data' not in request_data:
            return jsonify({
                'success': False,
                'error': 'Missing "data" field in request'
            }), 400
        
        data = request_data['data']
        
        if not isinstance(data, list):
            return jsonify({
                'success': False,
                'error': '"data" must be a list'
            }), 400
        
        if len(data) == 0:
            return jsonify({
                'success': False,
                'error': '"data" list is empty'
            }), 400
        
        # Make predictions
        results = predictor.predict_batch(data)
        
        return jsonify({
            'success': True,
            'total_predictions': len(results),
            'predictions': results
        }), 200
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': f'Invalid input value: {str(e)}'
        }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Batch prediction error: {str(e)}',
            'traceback': traceback.format_exc()
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("=" * 60)
    print("Crop Recommendation API Server")
    print("=" * 60)
    
    # Initialize predictor
    print("\nInitializing prediction model...")
    if initialize_predictor():
        print("[OK] Model loaded successfully!")
        print("\nStarting Flask server...")
        print("Server running at: http://localhost:5000")
        print("\nAPI Documentation:")
        print("  GET  /              - API info and endpoints")
        print("  GET  /health        - Health check")
        print("  GET  /crops         - List supported crops")
        print("  GET  /features      - List required features")
        print("  POST /predict       - Make single prediction")
        print("  POST /predict-batch - Make batch predictions")
        print("\n" + "=" * 60)
        
        # Run the app
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,
            use_reloader=False
        )
    else:
        print("[ERROR] Failed to load model!")
        print("Please train the model first using: python scripts/train.py")
