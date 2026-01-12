"""
Crop Recommendation Model Training Script

This script loads the crop recommendation dataset, preprocesses it,
trains a Random Forest classifier, and saves the trained model and scalers.
"""

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings

warnings.filterwarnings('ignore')

# Paths
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'Crop_recommendation.csv')
MODELS_PATH = os.path.join(os.path.dirname(__file__), '..', 'models')

# Create models directory if it doesn't exist
os.makedirs(MODELS_PATH, exist_ok=True)

print("=" * 60)
print("Crop Recommendation Model Training")
print("=" * 60)

# Step 1: Load the dataset
print("\n[1/6] Loading dataset...")
crop = pd.read_csv(DATA_PATH)
print(f"Dataset shape: {crop.shape}")
print(f"Columns: {list(crop.columns)}")
print(f"Unique crops: {crop['label'].nunique()}")

# Step 2: Data Preprocessing
print("\n[2/6] Preprocessing data...")

# Check for missing values
missing_values = crop.isnull().sum().sum()
print(f"Missing values: {missing_values}")

# Create mapping for crop labels
crop_dict = {
    'rice': 1,
    'maize': 2,
    'jute': 3,
    'cotton': 4,
    'coconut': 5,
    'papaya': 6,
    'orange': 7,
    'apple': 8,
    'muskmelon': 9,
    'watermelon': 10,
    'grapes': 11,
    'mango': 12,
    'banana': 13,
    'pomegranate': 14,
    'lentil': 15,
    'blackgram': 16,
    'mungbean': 17,
    'mothbeans': 18,
    'pigeonpeas': 19,
    'kidneybeans': 20,
    'chickpea': 21,
    'coffee': 22
}

# Encode labels
crop['label'] = crop['label'].map(crop_dict)
print(f"Label encoding completed. Classes: {sorted(crop['label'].unique())}")

# Step 3: Separate features and target
print("\n[3/6] Separating features and target...")
X = crop.drop('label', axis=1)
y = crop['label']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")
print(f"Feature columns: {list(X.columns)}")

# Step 4: Train-Test Split
print("\n[4/6] Splitting data (80-20)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

# Step 5: Feature Scaling
print("\n[5/6] Scaling features...")

# Apply MinMaxScaler
minmax_scaler = MinMaxScaler()
X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

# Apply StandardScaler
standard_scaler = StandardScaler()
X_train_scaled = standard_scaler.fit_transform(X_train_minmax)
X_test_scaled = standard_scaler.transform(X_test_minmax)

print("Feature scaling completed using MinMaxScaler + StandardScaler")

# Step 6: Train Random Forest Classifier
print("\n[6/6] Training Random Forest Classifier...")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    random_state=42,
    n_jobs=-1,
    verbose=0
)

model.fit(X_train_scaled, y_train)
print("Model training completed!")

# Predictions and Evaluation
print("\n" + "=" * 60)
print("Model Evaluation")
print("=" * 60)

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"\nClassification Report:")
# Only include labels that are actually in the test set
unique_labels = sorted(set(y_test) | set(y_pred))
crop_names = [k for k, v in crop_dict.items() if v in unique_labels]
print(classification_report(y_test, y_pred, labels=unique_labels, target_names=crop_names))

# Feature Importance
print("\n" + "=" * 60)
print("Feature Importance")
print("=" * 60)
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

print("\n", feature_importance.to_string(index=False))

# Save Models and Scalers
print("\n" + "=" * 60)
print("Saving Models and Scalers")
print("=" * 60)

try:
    # Save the trained model
    model_path = os.path.join(MODELS_PATH, 'crop_recommendation_model.pkl')
    pickle.dump(model, open(model_path, 'wb'))
    print(f"[OK] Model saved: {model_path}")
    
    # Save MinMaxScaler
    minmax_path = os.path.join(MODELS_PATH, 'minmax_scaler.pkl')
    pickle.dump(minmax_scaler, open(minmax_path, 'wb'))
    print(f"[OK] MinMaxScaler saved: {minmax_path}")
    
    # Save StandardScaler
    standard_path = os.path.join(MODELS_PATH, 'standard_scaler.pkl')
    pickle.dump(standard_scaler, open(standard_path, 'wb'))
    print(f"[OK] StandardScaler saved: {standard_path}")
    
    # Save crop mapping
    mapping_path = os.path.join(MODELS_PATH, 'crop_mapping.pkl')
    pickle.dump(crop_dict, open(mapping_path, 'wb'))
    print(f"[OK] Crop mapping saved: {mapping_path}")
    
    # Save feature names
    features_path = os.path.join(MODELS_PATH, 'feature_names.pkl')
    pickle.dump(list(X.columns), open(features_path, 'wb'))
    print(f"[OK] Feature names saved: {features_path}")
    
    print("\n[OK] All models and scalers saved successfully!")
    
except Exception as e:
    print(f"[ERROR] Error saving models: {e}")

print("\n" + "=" * 60)
print("Training Complete!")
print("=" * 60)
