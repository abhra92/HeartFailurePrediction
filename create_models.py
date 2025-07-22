# Create missing model files for testing
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

def create_sample_model_files():
    """Create sample model files for testing purposes."""
    
    # Create a simple trained model (dummy data)
    print("Creating sample model files...")
    
    # Feature names
    feature_names = [
        'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
        'ejection_fraction', 'high_blood_pressure', 'platelets',
        'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time'
    ]
    
    # Create and train a simple model with dummy data
    np.random.seed(42)
    X_dummy = np.random.randn(100, 12)  # 100 samples, 12 features
    y_dummy = np.random.randint(0, 2, 100)  # Binary classification
    
    # Train model
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_dummy, y_dummy)
    
    # Create scaler
    scaler = StandardScaler()
    scaler.fit(X_dummy)
    
    # Save model files
    with open('heart_failure_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("✅ Created heart_failure_model.pkl")
    
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print("✅ Created scaler.pkl")
    
    with open('feature_names.pkl', 'wb') as f:
        pickle.dump(feature_names, f)
    print("✅ Created feature_names.pkl")
    
    print("\n🎉 Sample model files created successfully!")
    print("⚠️  Note: These are dummy models for testing. Replace with real trained models for production.")
    
    return model, scaler, feature_names

if __name__ == "__main__":
    create_sample_model_files()
