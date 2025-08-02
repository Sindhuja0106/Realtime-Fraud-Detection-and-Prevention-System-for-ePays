#!/usr/bin/env python3
"""
Setup script for Fraud Detection and Prevention System
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies. Please check your Python environment.")
        return False
    return True

def check_model_file():
    """Check if the model file exists"""
    if not os.path.exists('rf_model3.pkl'):
        print("⚠️  Warning: Model file 'rf_model3.pkl' not found!")
        print("   The application may not work properly without the trained model.")
        return False
    print("✅ Model file found!")
    return True

def run_app():
    """Run the Streamlit application"""
    print("🚀 Starting the Fraud Detection Application...")
    print("📱 The app will open in your browser at http://localhost:8501")
    print("🔄 To stop the app, press Ctrl+C in this terminal")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"❌ Error running the application: {e}")

def main():
    print("🛡️  Fraud Detection and Prevention System Setup")
    print("=" * 50)
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check model file
    check_model_file()
    
    print("\n🎯 Setup complete! You can now:")
    print("1. Run 'python setup.py' to start the application")
    print("2. Or run 'streamlit run app.py' directly")
    print("3. Or use the 'run_app()' function in this script")
    
    # Ask if user wants to run the app
    response = input("\n🚀 Would you like to start the application now? (y/n): ").lower()
    if response in ['y', 'yes']:
        run_app()

if __name__ == "__main__":
    main() 