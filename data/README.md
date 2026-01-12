# Data Directory

This directory should contain your crop and climate data files.

## Expected Data Format

Your CSV file should contain the following columns:

### Climate Features (example columns):
- `N` - Nitrogen content in soil
- `P` - Phosphorus content in soil
- `K` - Potassium content in soil
- `temperature` - Temperature in Celsius
- `humidity` - Relative humidity in %
- `ph` - pH value of the soil
- `rainfall` - Rainfall in mm

### Target Variable:
- `label` - Crop name (e.g., rice, wheat, maize, etc.)

## Sample Data Structure

```csv
N,P,K,temperature,humidity,ph,rainfall,label
90,42,43,20.87,82.00,6.50,202.93,rice
85,58,41,21.77,80.31,7.03,226.65,rice
60,55,44,23.00,82.32,7.84,263.96,rice
...
```

## Adding Your Data

1. Place your CSV file in this directory
2. Update the file path in `crop_prediction.py` if needed
3. Ensure your CSV has a 'label' column for crop names

## Note

Large data files (*.csv) are ignored by git. Add a sample or small dataset for testing purposes.
