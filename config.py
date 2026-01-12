"""
Configuration file for Crop Recommendation System
"""

import os

# Project paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(PROJECT_ROOT, 'data')
MODELS_PATH = os.path.join(PROJECT_ROOT, 'models')
SCRIPTS_PATH = os.path.join(PROJECT_ROOT, 'scripts')

# Data file
DATASET_FILE = os.path.join(DATA_PATH, 'Crop_recommendation.csv')

# Model files
MODEL_FILE = os.path.join(MODELS_PATH, 'crop_recommendation_model.pkl')
MINMAX_SCALER_FILE = os.path.join(MODELS_PATH, 'minmax_scaler.pkl')
STANDARD_SCALER_FILE = os.path.join(MODELS_PATH, 'standard_scaler.pkl')
CROP_MAPPING_FILE = os.path.join(MODELS_PATH, 'crop_mapping.pkl')
FEATURE_NAMES_FILE = os.path.join(MODELS_PATH, 'feature_names.pkl')

# Model hyperparameters
MODEL_PARAMS = {
    'n_estimators': 100,
    'max_depth': 20,
    'random_state': 42,
    'n_jobs': -1,
    'verbose': 0
}

# Train-test split ratio
TEST_SIZE = 0.2
RANDOM_STATE = 42

# API configuration
API_HOST = '0.0.0.0'
API_PORT = 5000
API_DEBUG = False

# Supported crops
CROPS = {
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

# Feature names (in order)
FEATURES = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Feature ranges for validation
FEATURE_RANGES = {
    'N': (0, 300),
    'P': (0, 300),
    'K': (0, 300),
    'temperature': (10, 35),
    'humidity': (20, 100),
    'ph': (5.0, 8.0),
    'rainfall': (50, 500)
}

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
