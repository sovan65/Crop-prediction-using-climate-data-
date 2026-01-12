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
                'data': [90, 42, 43, 20.87, 82.00, 6.50, 202.93]
            },
            {
                'name': 'Low Rainfall, High Temperature',
                'data': [40, 60, 50, 30.5, 65.0, 7.2, 85.0]
            },
            {
                'name': 'Moderate Conditions',
                'data': [70, 50, 45, 25.0, 75.0, 6.8, 150.0]
            }
        ]
        
        print("\nPredicting suitable crops for different scenarios:\n")
        
        for scenario in scenarios:
            predicted_crop = predictor.predict_crop(scenario['data'])
            print(f"Scenario: {scenario['name']}")
            print(f"  Climate Data: N={scenario['data'][0]}, P={scenario['data'][1]}, "
                  f"K={scenario['data'][2]}, Temp={scenario['data'][3]}°C, "
                  f"Humidity={scenario['data'][4]}%, pH={scenario['data'][5]}, "
                  f"Rainfall={scenario['data'][6]}mm")
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
