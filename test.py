"""
Test script for Crop Recommendation System

This script tests the trained model with various inputs and validates the system.
"""

import sys
import os

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from predict import CropRecommendationPredictor

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_basic_prediction():
    """Test basic single prediction."""
    print_header("Test 1: Basic Single Prediction")
    
    predictor = CropRecommendationPredictor()
    
    # Test case: Rice growing conditions
    result = predictor.predict(
        N=90,
        P=42,
        K=43,
        temperature=20.88,
        humidity=82.00,
        ph=6.50,
        rainfall=202.94
    )
    
    print(f"\nInput Conditions:")
    print(f"  Nitrogen (N): {result['input']['N']} kg/ha")
    print(f"  Phosphorus (P): {result['input']['P']} kg/ha")
    print(f"  Potassium (K): {result['input']['K']} kg/ha")
    print(f"  Temperature: {result['input']['temperature']}°C")
    print(f"  Humidity: {result['input']['humidity']}%")
    print(f"  pH: {result['input']['ph']}")
    print(f"  Rainfall: {result['input']['rainfall']} mm")
    
    print(f"\nPrediction Result:")
    print(f"  Recommended Crop: {result['crop'].upper()}")
    print(f"  Crop ID: {result['crop_id']}")
    print(f"  Confidence: {result['confidence']}%")
    
    return result['crop'] == 'rice'

def test_mango_prediction():
    """Test mango growing conditions."""
    print_header("Test 2: Mango Growing Conditions")
    
    predictor = CropRecommendationPredictor()
    
    # Test case: Mango growing conditions
    result = predictor.predict(
        N=120,
        P=70,
        K=50,
        temperature=28.0,
        humidity=65.0,
        ph=6.5,
        rainfall=200.0
    )
    
    print(f"\nInput Conditions:")
    print(f"  Nitrogen (N): {result['input']['N']} kg/ha")
    print(f"  Phosphorus (P): {result['input']['P']} kg/ha")
    print(f"  Potassium (K): {result['input']['K']} kg/ha")
    print(f"  Temperature: {result['input']['temperature']}°C")
    print(f"  Humidity: {result['input']['humidity']}%")
    print(f"  pH: {result['input']['ph']}")
    print(f"  Rainfall: {result['input']['rainfall']} mm")
    
    print(f"\nPrediction Result:")
    print(f"  Recommended Crop: {result['crop'].upper()}")
    print(f"  Confidence: {result['confidence']}%")
    
    return result['crop'] == 'mango'

def test_apple_prediction():
    """Test apple growing conditions."""
    print_header("Test 3: Apple Growing Conditions")
    
    predictor = CropRecommendationPredictor()
    
    # Test case: Apple growing conditions
    result = predictor.predict(
        N=100,
        P=60,
        K=40,
        temperature=20.0,
        humidity=50.0,
        ph=6.5,
        rainfall=90.0
    )
    
    print(f"\nInput Conditions:")
    print(f"  Nitrogen (N): {result['input']['N']} kg/ha")
    print(f"  Phosphorus (P): {result['input']['P']} kg/ha")
    print(f"  Potassium (K): {result['input']['K']} kg/ha")
    print(f"  Temperature: {result['input']['temperature']}°C")
    print(f"  Humidity: {result['input']['humidity']}%")
    print(f"  pH: {result['input']['ph']}")
    print(f"  Rainfall: {result['input']['rainfall']} mm")
    
    print(f"\nPrediction Result:")
    print(f"  Recommended Crop: {result['crop'].upper()}")
    print(f"  Confidence: {result['confidence']}%")
    
    return result['crop'] == 'apple'

def test_batch_prediction():
    """Test batch predictions."""
    print_header("Test 4: Batch Predictions")
    
    predictor = CropRecommendationPredictor()
    
    # Multiple test cases
    test_data = [
        {
            'N': 90, 'P': 42, 'K': 43,
            'temperature': 20.88, 'humidity': 82.00,
            'ph': 6.50, 'rainfall': 202.94,
            'expected': 'rice'
        },
        {
            'N': 120, 'P': 70, 'K': 50,
            'temperature': 28.0, 'humidity': 65.0,
            'ph': 6.5, 'rainfall': 200.0,
            'expected': 'mango'
        },
        {
            'N': 100, 'P': 60, 'K': 40,
            'temperature': 20.0, 'humidity': 50.0,
            'ph': 6.5, 'rainfall': 90.0,
            'expected': 'apple'
        }
    ]
    
    results = predictor.predict_batch(test_data)
    
    print(f"\nTotal Predictions: {len(results)}\n")
    
    correct = 0
    for i, (test, result) in enumerate(zip(test_data, results), 1):
        expected = test['expected'].upper()
        predicted = result['crop'].upper()
        confidence = result['confidence']
        
        match = "✓" if predicted == expected else "✗"
        print(f"{match} Test {i}:")
        print(f"    Expected: {expected}")
        print(f"    Predicted: {predicted}")
        print(f"    Confidence: {confidence}%")
        
        if predicted == expected:
            correct += 1
    
    accuracy = (correct / len(results)) * 100
    print(f"\nBatch Accuracy: {correct}/{len(results)} ({accuracy:.1f}%)")
    
    return correct == len(results)

def test_crop_list():
    """Test getting crop information."""
    print_header("Test 5: Crop Information")
    
    predictor = CropRecommendationPredictor()
    crops = predictor.get_crop_info()
    
    print(f"\nTotal Supported Crops: {len(crops)}\n")
    
    for i, (crop_name, crop_id) in enumerate(sorted(crops.items(), key=lambda x: x[1]), 1):
        print(f"{crop_id:2d}. {crop_name.capitalize()}")
    
    return len(crops) == 22

def test_feature_names():
    """Test getting feature names."""
    print_header("Test 6: Feature Names")
    
    predictor = CropRecommendationPredictor()
    features = predictor.get_feature_names()
    
    print(f"\nRequired Features: {len(features)}")
    for i, feature in enumerate(features, 1):
        print(f"  {i}. {feature}")
    
    expected_features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    return features == expected_features

def run_all_tests():
    """Run all tests and report results."""
    print_header("CROP RECOMMENDATION SYSTEM - TEST SUITE")
    
    tests = [
        ("Basic Single Prediction", test_basic_prediction),
        ("Mango Prediction", test_mango_prediction),
        ("Apple Prediction", test_apple_prediction),
        ("Batch Predictions", test_batch_prediction),
        ("Crop List", test_crop_list),
        ("Feature Names", test_feature_names),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed, None))
        except Exception as e:
            results.append((test_name, False, str(e)))
    
    # Print summary
    print_header("TEST SUMMARY")
    
    passed_count = sum(1 for _, passed, _ in results if passed)
    total_count = len(results)
    
    print(f"\nTotal Tests: {total_count}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {total_count - passed_count}\n")
    
    for test_name, passed, error in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")
        if error:
            print(f"       Error: {error}")
    
    print("\n" + "=" * 70)
    
    if passed_count == total_count:
        print("All tests passed! ✓")
        return 0
    else:
        print(f"{total_count - passed_count} test(s) failed.")
        return 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
