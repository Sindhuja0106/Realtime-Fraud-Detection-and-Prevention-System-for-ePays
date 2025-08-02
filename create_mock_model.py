#!/usr/bin/env python3
"""
Create a mock Random Forest model for testing the fraud detection system
"""

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def create_mock_model():
    """Create a simple mock Random Forest model for testing"""
    print("🤖 Creating mock Random Forest model...")
    
    # Generate mock training data
    np.random.seed(42)
    n_samples = 1000
    
    # Create synthetic transaction data
    step = np.random.randint(1, 100, n_samples)
    amount = np.random.uniform(100, 100000, n_samples)
    oldbalanceOrg = np.random.uniform(0, 200000, n_samples)
    newbalanceOrig = oldbalanceOrg - amount
    oldbalanceDest = np.random.uniform(0, 200000, n_samples)
    newbalanceDest = oldbalanceDest + amount
    isFlaggedFraud = np.random.choice([0, 1], n_samples, p=[0.95, 0.05])
    
    # Create features
    X = np.column_stack([step, amount, oldbalanceOrg, newbalanceOrig, 
                         oldbalanceDest, newbalanceDest, isFlaggedFraud])
    
    # Create target (fraud labels) based on some rules
    y = np.zeros(n_samples)
    
    # Simple fraud detection rules for mock data
    for i in range(n_samples):
        fraud_score = 0
        
        # High amount transactions
        if amount[i] > 50000:
            fraud_score += 1
            
        # Large balance changes
        if abs(newbalanceOrig[i] - oldbalanceOrg[i]) > 40000:
            fraud_score += 1
            
        # Zero destination balance
        if oldbalanceDest[i] == 0 and newbalanceDest[i] == 0:
            fraud_score += 1
            
        # Flagged transactions
        if isFlaggedFraud[i] == 1:
            fraud_score += 1
            
        # Mark as fraud if score is high enough
        if fraud_score >= 2:
            y[i] = 1
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the model
    rf_model = RandomForestClassifier(
        n_estimators=45,
        max_depth=4,
        min_samples_split=100,
        min_samples_leaf=30,
        random_state=42
    )
    
    # Train the model
    rf_model.fit(X_train, y_train)
    
    # Evaluate the model
    train_score = rf_model.score(X_train, y_train)
    test_score = rf_model.score(X_test, y_test)
    
    print(f"✅ Model created successfully!")
    print(f"📊 Training accuracy: {train_score:.3f}")
    print(f"📊 Test accuracy: {test_score:.3f}")
    
    # Save the model
    joblib.dump(rf_model, 'rf_model3.pkl')
    print("💾 Model saved as 'rf_model3.pkl'")
    
    return rf_model

if __name__ == "__main__":
    create_mock_model() 