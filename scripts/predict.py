"""
Crop Recommendation Prediction Module

This module handles making predictions using the trained model.
It loads the saved model, scalers, and makes predictions for new crop conditions.
"""

import pickle
import numpy as np
import os
from pathlib import Path

# Paths
MODELS_PATH = os.path.join(os.path.dirname(__file__), '..', 'models')

class CropRecommendationPredictor:
    """
    A class to handle crop recommendation predictions.
    """
    
    def __init__(self):
        """Initialize the predictor by loading model and scalers."""
        self.model = None
        self.minmax_scaler = None
        self.standard_scaler = None
        self.crop_mapping = None
        self.reverse_crop_mapping = None
        self.feature_names = None
        
        self._load_models()
    
    def _load_models(self):
        """Load the trained model and scalers from disk."""
        try:
            model_path = os.path.join(MODELS_PATH, 'crop_recommendation_model.pkl')
            minmax_path = os.path.join(MODELS_PATH, 'minmax_scaler.pkl')
            standard_path = os.path.join(MODELS_PATH, 'standard_scaler.pkl')
            mapping_path = os.path.join(MODELS_PATH, 'crop_mapping.pkl')
            features_path = os.path.join(MODELS_PATH, 'feature_names.pkl')
            
            # Load model
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model not found at {model_path}")
            self.model = pickle.load(open(model_path, 'rb'))
            
            # Load scalers
            if not os.path.exists(minmax_path):
                raise FileNotFoundError(f"MinMaxScaler not found at {minmax_path}")
            self.minmax_scaler = pickle.load(open(minmax_path, 'rb'))
            
            if not os.path.exists(standard_path):
                raise FileNotFoundError(f"StandardScaler not found at {standard_path}")
            self.standard_scaler = pickle.load(open(standard_path, 'rb'))
            
            # Load crop mapping
            if not os.path.exists(mapping_path):
                raise FileNotFoundError(f"Crop mapping not found at {mapping_path}")
            self.crop_mapping = pickle.load(open(mapping_path, 'rb'))
            self.reverse_crop_mapping = {v: k for k, v in self.crop_mapping.items()}
            
            # Load feature names
            if not os.path.exists(features_path):
                raise FileNotFoundError(f"Feature names not found at {features_path}")
            self.feature_names = pickle.load(open(features_path, 'rb'))
            
            print("✓ All models loaded successfully!")
            
        except Exception as e:
            raise RuntimeError(f"Error loading models: {e}")
    
    def predict(self, N, P, K, temperature, humidity, ph, rainfall):
        """
        Predict the best crop recommendation based on given conditions.
        
        Parameters:
        -----------
        N : float
            Nitrogen content (kg/ha)
        P : float
            Phosphorus content (kg/ha)
        K : float
            Potassium content (kg/ha)
        temperature : float
            Temperature (°C)
        humidity : float
            Humidity (%)
        ph : float
            pH level
        rainfall : float
            Rainfall (mm)
        
        Returns:
        --------
        dict : Contains predicted crop name and probability confidence
        """
        
        try:
            # Create feature array
            features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            
            # Apply MinMaxScaler
            features_minmax = self.minmax_scaler.transform(features)
            
            # Apply StandardScaler
            features_scaled = self.standard_scaler.transform(features_minmax)
            
            # Make prediction
            prediction_label = self.model.predict(features_scaled)[0]
            
            # Get prediction probabilities
            prediction_proba = self.model.predict_proba(features_scaled)
            max_confidence = np.max(prediction_proba) * 100
            
            # Convert label to crop name
            crop_name = self.reverse_crop_mapping[prediction_label]
            
            return {
                'crop': crop_name,
                'crop_id': int(prediction_label),
                'confidence': round(max_confidence, 2),
                'input': {
                    'N': N,
                    'P': P,
                    'K': K,
                    'temperature': temperature,
                    'humidity': humidity,
                    'ph': ph,
                    'rainfall': rainfall
                }
            }
        
        except Exception as e:
            raise RuntimeError(f"Error during prediction: {e}")
    
    def predict_batch(self, data):
        """
        Make predictions for a batch of data.
        
        Parameters:
        -----------
        data : list of dict
            List of dictionaries containing features
        
        Returns:
        --------
        list : List of prediction results
        """
        results = []
        for row in data:
            result = self.predict(
                row['N'],
                row['P'],
                row['K'],
                row['temperature'],
                row['humidity'],
                row['ph'],
                row['rainfall']
            )
            results.append(result)
        
        return results
    
    def get_crop_info(self):
        """
        Get information about all supported crops.
        
        Returns:
        --------
        dict : Mapping of crop names to IDs
        """
        return self.crop_mapping
    
    def get_feature_names(self):
        """
        Get the list of feature names used by the model.
        
        Returns:
        --------
        list : List of feature names
        """
        return self.feature_names


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Crop Recommendation Prediction System")
    print("=" * 60)
    
    # Initialize predictor
    predictor = CropRecommendationPredictor()
    
    # Example prediction
    print("\n[Example 1] Predicting crop for:")
    print("N=90, P=42, K=43, Temp=20.88, Humidity=82.0, pH=6.5, Rainfall=202.94")
    
    result = predictor.predict(
        N=90,
        P=42,
        K=43,
        temperature=20.879744,
        humidity=82.002744,
        ph=6.502985,
        rainfall=202.935536
    )
    
    print(f"\n✓ Predicted Crop: {result['crop']}")
    print(f"✓ Confidence: {result['confidence']}%")
    
    # Another example
    print("\n" + "=" * 60)
    print("[Example 2] Predicting crop for different conditions:")
    print("N=120, P=70, K=50, Temp=28.0, Humidity=65.0, pH=6.5, Rainfall=200.0")
    
    result2 = predictor.predict(
        N=120,
        P=70,
        K=50,
        temperature=28.0,
        humidity=65.0,
        ph=6.5,
        rainfall=200.0
    )
    
    print(f"\n✓ Predicted Crop: {result2['crop']}")
    print(f"✓ Confidence: {result2['confidence']}%")
    
    # List all supported crops
    print("\n" + "=" * 60)
    print("Supported Crops:")
    print("=" * 60)
    crops = predictor.get_crop_info()
    for crop, crop_id in sorted(crops.items(), key=lambda x: x[1]):
        print(f"{crop_id:2d}. {crop}")
