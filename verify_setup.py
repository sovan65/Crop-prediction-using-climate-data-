#!/usr/bin/env python3
"""
Setup verification script for Crop Prediction system
Checks if all dependencies and files are properly configured
"""

import sys
import os

def check_dependencies():
    """Check if all required Python packages are installed"""
    print("Checking Python dependencies...")
    required_packages = [
        'numpy',
        'pandas', 
        'sklearn',
        'matplotlib',
        'seaborn',
        'joblib'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} (missing)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install -r requirements.txt")
        return False
    return True

def check_directory_structure():
    """Check if required directories exist"""
    print("\nChecking directory structure...")
    required_dirs = ['data', 'models']
    
    all_exist = True
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"  ✓ {dir_name}/")
        else:
            print(f"  ✗ {dir_name}/ (missing)")
            all_exist = False
    
    return all_exist

def check_files():
    """Check if required files exist"""
    print("\nChecking required files...")
    required_files = [
        'crop_prediction.py',
        'requirements.txt',
        'README.md',
        '.gitignore'
    ]
    
    all_exist = True
    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"  ✓ {file_name}")
        else:
            print(f"  ✗ {file_name} (missing)")
            all_exist = False
    
    return all_exist

def check_data():
    """Check if data file exists"""
    print("\nChecking for data file...")
    if os.path.exists('data/crop_data.csv'):
        print("  ✓ data/crop_data.csv found")
        return True
    else:
        print("  ℹ data/crop_data.csv not found (this is optional)")
        print("    Add your dataset to data/crop_data.csv to train the model")
        return True  # This is not a critical error

def main():
    """Run all verification checks"""
    print("=" * 60)
    print("Crop Prediction System - Setup Verification")
    print("=" * 60)
    print()
    
    checks = [
        ("Python version", sys.version_info >= (3, 7)),
        ("Dependencies", check_dependencies()),
        ("Directory structure", check_directory_structure()),
        ("Required files", check_files()),
        ("Data files", check_data())
    ]
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    all_passed = True
    for check_name, result in checks:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {check_name}")
        if not result:
            all_passed = False
    
    print()
    if all_passed:
        print("✓ All checks passed! The system is ready to use.")
        print("\nNext steps:")
        print("1. Add your crop data to data/crop_data.csv")
        print("2. Run: python crop_prediction.py")
        print("3. Or see example.py for usage examples")
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
