"""
Crop Prediction Using Climate Data
This module provides functionality to predict suitable crops based on climate parameters.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os


class CropPredictor:
    """
    A class for predicting crops based on climate data.
    
    Attributes:
        model: The trained machine learning model
        scaler: StandardScaler for feature normalization
        crop_labels: List of crop names
    """
    
    # Expected feature order for consistent predictions
    FEATURE_KEYS = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.crop_labels = []
    
    def load_data(self, filepath):
        """
        Load crop and climate data from a CSV file.
        
        Args:
            filepath: Path to the CSV file containing crop data
            
        Returns:
            DataFrame with loaded data
        """
        try:
            data = pd.read_csv(filepath)
            print(f"Data loaded successfully with {len(data)} records")
            return data
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return None
    
    def prepare_data(self, data, target_column='label'):
        """
        Prepare data for training by splitting features and target.
        
        Args:
            data: Input DataFrame
            target_column: Name of the target column
            
        Returns:
            Tuple of (X_train, X_test, y_train, y_test)
        """
        if data is None:
            return None, None, None, None
        
        # Validate target column exists
        if target_column not in data.columns:
            print(f"Error: Target column '{target_column}' not found in data")
            return None, None, None, None
        
        # Separate features and target
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        
        # Store crop labels
        self.crop_labels = list(y.unique())
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)
        
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):
        """
        Train the Random Forest model.
        
        Args:
            X_train: Training features
            y_train: Training labels
        """
        print("Training model...")
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=10
        )
        self.model.fit(X_train, y_train)
        print("Model training completed!")
    
    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the trained model.
        
        Args:
            X_test: Test features
            y_test: Test labels
            
        Returns:
            Accuracy score
        """
        if self.model is None:
            print("Error: Model not trained yet")
            return 0
        
        accuracy = self.model.score(X_test, y_test)
        print(f"Model Accuracy: {accuracy * 100:.2f}%")
        return accuracy
    
    def predict_crop(self, climate_data):
        """
        Predict the best crop for given climate conditions.
        
        Args:
            climate_data: Dictionary or array of climate parameters
                         If dict, expected keys: N, P, K, temperature, humidity, ph, rainfall
            
        Returns:
            Predicted crop name
        """
        if self.model is None:
            print("Error: Model not trained yet")
            return None
        
        # Convert to array if dictionary
        if isinstance(climate_data, dict):
            # Use explicit key order to ensure consistency
            try:
                climate_data = np.array([climate_data[key] for key in self.FEATURE_KEYS]).reshape(1, -1)
            except KeyError as e:
                print(f"Error: Missing required key {e} in climate_data")
                print(f"Expected keys: {self.FEATURE_KEYS}")
                return None
        else:
            climate_data = np.array(climate_data).reshape(1, -1)
        
        # Scale the input
        climate_data_scaled = self.scaler.transform(climate_data)
        
        # Predict
        prediction = self.model.predict(climate_data_scaled)
        return prediction[0]
    
    def save_model(self, model_path='models/crop_predictor.pkl'):
        """
        Save the trained model to disk.
        
        Args:
            model_path: Path where the model will be saved
        """
        if self.model is None:
            print("Error: No model to save")
            return
        
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'crop_labels': self.crop_labels
        }
        joblib.dump(model_data, model_path)
        print(f"Model saved to {model_path}")
    
    def load_model(self, model_path='models/crop_predictor.pkl'):
        """
        Load a trained model from disk.
        
        Args:
            model_path: Path to the saved model
        """
        try:
            model_data = joblib.load(model_path)
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.crop_labels = model_data['crop_labels']
            print(f"Model loaded from {model_path}")
        except FileNotFoundError:
            print(f"Error: Model file not found at {model_path}")


def main():
    """
    Main function to demonstrate the crop prediction system.
    """
    print("=" * 50)
    print("Crop Prediction Using Climate Data")
    print("=" * 50)
    
    # Initialize predictor
    predictor = CropPredictor()
    
    # Example: Check if data file exists
    data_path = 'data/crop_data.csv'
    if os.path.exists(data_path):
        # Load and prepare data
        data = predictor.load_data(data_path)
        
        if data is not None:
            X_train, X_test, y_train, y_test = predictor.prepare_data(data)
            
            # Train model
            predictor.train_model(X_train, y_train)
            
            # Evaluate model
            predictor.evaluate_model(X_test, y_test)
            
            # Save model
            predictor.save_model()
            
            print("\nModel training complete!")
            print(f"Crops in dataset: {predictor.crop_labels}")
    else:
        print(f"\nNote: Sample data file not found at {data_path}")
        print("Please add your crop data CSV file to the 'data' directory.")
        print("\nExpected format: CSV with climate features and a 'label' column for crop names")
        print("Example features: temperature, humidity, rainfall, pH, etc.")


if __name__ == "__main__":
    main()
