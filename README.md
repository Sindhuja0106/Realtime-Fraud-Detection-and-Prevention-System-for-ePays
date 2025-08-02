# 🛡️ Fraud Detection and Prevention System for ePay

A comprehensive machine learning-based fraud detection system built with Streamlit for real-time transaction monitoring and fraud prevention.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## 🎯 Overview

This application predicts fraudulent transactions in online payment systems using advanced machine learning techniques. Designed for real-time fraud detection and prevention, it empowers financial institutions and e-commerce platforms to identify suspicious activities instantly.

### Key Objectives
- ✅ Enhance user trust and platform credibility
- 💸 Reduce financial losses
- 🛡️ Comply with regulatory security standards

## ✨ Features

### 1. Real-Time Fraud Detection
- Detects fraud during transaction processing by analyzing transaction features like amount, origin, and time
- Provides immediate feedback to help prevent fraudulent activities

### 2. Interactive Interface
- Powered by Streamlit, users can easily input transaction details to get predictions
- Designed for accessibility and user-friendliness, ensuring a seamless experience

### 3. Comprehensive Feature Engineering
- Implements advanced preprocessing steps to clean and optimize transaction data
- Handles missing values, scaling amounts, and encoding categorical variables

### 4. Advanced Analytics
- Exploratory Data Analysis (EDA) with interactive visualizations
- Outlier detection and removal using Z-Score and IQR methods
- Correlation analysis and feature importance visualization

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fraud-detection-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:8501`

## 📖 Usage

### Single Transaction Analysis
1. Navigate to the "Getting Started" section
2. Enter transaction details:
   - **Step**: Time step of the transaction
   - **Amount**: Transaction amount
   - **Old Balance (Origin)**: Original balance in the origin account
   - **New Balance (Origin)**: New balance in the origin account after transaction
   - **Old Balance (Destination)**: Original balance in the destination account
   - **New Balance (Destination)**: New balance in the destination account after transaction
   - **Is Flagged as Fraud**: Whether the transaction was internally flagged (0/1)

3. Click "Detect Fraud and View Results" to get predictions

### Bulk Transaction Analysis
1. Prepare a CSV file with the required columns:
   - `step`, `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`, `isFlaggedFraud`
2. Upload the file through the bulk analysis interface
3. View comprehensive results and download analysis reports

### Sample Data
The project includes sample CSV files:
- `sample_bulk_transactions.csv`: Example transactions for testing
- `obvious_fraud_transactions.csv`: Known fraudulent transactions for validation

## 📁 Project Structure

```
fraud-detection-system/
├── app.py                 # Main Streamlit application
├── front6.py             # Fraud detection interface module
├── visualizations.py     # Data visualization module
├── csv_utils.py         # CSV processing utilities
├── requirements.txt      # Python dependencies
├── rf_model3.pkl        # Trained Random Forest model
├── README.md            # Project documentation
├── img/                 # Image assets directory
├── sample_bulk_transactions.csv      # Sample transaction data
└── obvious_fraud_transactions.csv    # Known fraud data
```

## 🤖 Model Details

### Random Forest Model
- **Algorithm**: Random Forest (Ensemble of Decision Trees)
- **Library**: scikit-learn's `RandomForestClassifier`
- **AUC-ROC Score**: 0.9556
- **Accuracy**: ~96% on test set
- **Precision**: ~49% for fraud detection
- **F1-Score**: ~65%

### Features Used
- `step`: Time step of the transaction
- `amount`: Transaction amount
- `oldbalanceOrg`: Original balance in the origin account before the transaction
- `newbalanceOrig`: New balance in the origin account after the transaction
- `oldbalanceDest`: Original balance in the destination account before the transaction
- `newbalanceDest`: New balance in the destination account after the transaction
- `isFlaggedFraud`: Indicates whether the transaction was internally flagged as potentially fraudulent

### Hyperparameters
- `n_estimators`: 45 (number of trees in the forest)
- `max_depth`: 4 (maximum depth of each tree)
- `min_samples_split`: 100 (minimum samples required to split a node)
- `min_samples_leaf`: 30 (minimum samples required at a leaf node)
- `random_state`: 42 (for reproducibility)

## 📊 Data Visualization

The application includes comprehensive visualizations:

### Data Exploration
- Transaction Types distribution
- Fraud vs. Flagged Fraud analysis
- Percentage of Fraud by Hour
- KDE Plot of Amount by Class

### Outlier Analysis
- Outlier detection plots
- Outlier handling visualizations

### Correlation Analysis
- Correlation Matrix
- Transaction Amount Distribution

## 🔧 API Documentation

### Main Functions

#### `detect_fraud(transaction)`
Detects fraud in a single transaction.

**Parameters:**
- `transaction` (list): List containing transaction features

**Returns:**
- `prediction` (int): 1 for fraud, 0 for legitimate
- `reason` (str): Explanation for the prediction
- `issues` (dict): Dictionary indicating origin/destination issues

#### `prevent_fraud(transaction)`
Provides prevention advice for a transaction.

**Parameters:**
- `transaction` (list): List containing transaction features

**Returns:**
- `action` (str): Prevention advice or "✅ ALLOWED"

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions, please contact the development team or create an issue in the repository.

---

**Note**: This system is designed for educational and demonstration purposes. For production use, additional security measures and compliance checks should be implemented. 