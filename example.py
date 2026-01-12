"""
Example usage of the Crop Prediction system
This script demonstrates how to use the CropPredictor class
"""

from crop_prediction import CropPredictor
import numpy as np

def example_prediction():
    """
    Demonstrate crop prediction with sample climate data
    """
    print("=" * 60)
    print("Crop Prediction Example")
    print("=" * 60)
    
    # Initialize predictor
    predictor = CropPredictor()
    
    # Check if a trained model exists
    try:
        predictor.load_model('models/crop_predictor.pkl')
        print("\nLoaded existing model successfully!")
        
        # Example climate scenarios
        scenarios = [
            {
                'name': 'High Rainfall, Moderate Temperature',
                'data': {
                    'N': 90, 'P': 42, 'K': 43,
                    'temperature': 20.87, 'humidity': 82.00,
                    'ph': 6.50, 'rainfall': 202.93
                }
            },
            {
                'name': 'Low Rainfall, High Temperature',
                'data': {
                    'N': 40, 'P': 60, 'K': 50,
                    'temperature': 30.5, 'humidity': 65.0,
                    'ph': 7.2, 'rainfall': 85.0
                }
            },
            {
                'name': 'Moderate Conditions',
                'data': {
                    'N': 70, 'P': 50, 'K': 45,
                    'temperature': 25.0, 'humidity': 75.0,
                    'ph': 6.8, 'rainfall': 150.0
                }
            }
        ]
        
        print("\nPredicting suitable crops for different scenarios:\n")
        
        for scenario in scenarios:
            predicted_crop = predictor.predict_crop(scenario['data'])
            data = scenario['data']
            print(f"Scenario: {scenario['name']}")
            print(f"  Climate Data: N={data['N']}, P={data['P']}, "
                  f"K={data['K']}, Temp={data['temperature']}°C, "
                  f"Humidity={data['humidity']}%, pH={data['ph']}, "
                  f"Rainfall={data['rainfall']}mm")
            print(f"  ✓ Recommended Crop: {predicted_crop}")
            print()
        
    except Exception as e:
        print(f"\nNo trained model found. Error: {str(e)}")
        print("\nTo use this example:")
        print("1. Add your crop dataset to data/crop_data.csv")
        print("2. Run: python crop_prediction.py")
        print("3. This will train and save a model")
        print("4. Then run this example script again")

def example_training():
    """
    Example of how to train a model with custom data
    """
    print("\n" + "=" * 60)
    print("Training Example")
    print("=" * 60)
    print("\nNote: This requires a dataset at data/crop_data.csv")
    print("\nSteps to train your own model:")
    print("1. Prepare your CSV file with columns: N, P, K, temperature, humidity, ph, rainfall, label")
    print("2. Place it in the data/ directory as crop_data.csv")
    print("3. Run: python crop_prediction.py")
    print("4. The model will be saved to models/crop_predictor.pkl")


if __name__ == "__main__":
    example_prediction()
    example_training()
