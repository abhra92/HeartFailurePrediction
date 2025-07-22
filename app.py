from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
try:
    with open('heart_failure_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    with open('feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    
    print("✅ Model and scaler loaded successfully!")
    print(f"Model type: {type(model).__name__}")
    print(f"Features: {feature_names}")
    
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    scaler = None
    feature_names = None

@app.route('/')
def home():
    """Render the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        if model is None:
            return jsonify({
                'error': 'Model not loaded properly',
                'success': False
            })
        
        # Get form data
        form_data = request.form
        
        # Extract features in the correct order
        features = [
            float(form_data['age']),
            int(form_data['anaemia']),
            float(form_data['creatinine_phosphokinase']),
            int(form_data['diabetes']),
            float(form_data['ejection_fraction']),
            int(form_data['high_blood_pressure']),
            float(form_data['platelets']),
            float(form_data['serum_creatinine']),
            float(form_data['serum_sodium']),
            int(form_data['sex']),
            int(form_data['smoking']),
            float(form_data['time'])
        ]
        
        # Convert to numpy array
        input_data = np.array(features).reshape(1, -1)
        
        # Create DataFrame with proper column names
        input_df = pd.DataFrame(input_data, columns=feature_names)
        
        # Check if we need to scale the data (for SVM or Logistic Regression)
        model_name = type(model).__name__
        if model_name in ['SVC', 'LogisticRegression']:
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0]
        else:
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
        
        # Get prediction probability
        death_probability = probability[1] * 100  # Probability of death event
        survival_probability = probability[0] * 100  # Probability of survival
        
        # Prepare result
        result = {
            'prediction': int(prediction),
            'death_probability': round(death_probability, 2),
            'survival_probability': round(survival_probability, 2),
            'risk_level': get_risk_level(death_probability),
            'success': True
        }
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({
            'error': f'Prediction error: {str(e)}',
            'success': False
        })

def get_risk_level(death_probability):
    """Determine risk level based on death probability"""
    if death_probability < 20:
        return {'level': 'Low', 'color': 'success', 'description': 'Low risk of heart failure complications'}
    elif death_probability < 40:
        return {'level': 'Moderate', 'color': 'warning', 'description': 'Moderate risk - monitor closely'}
    elif death_probability < 60:
        return {'level': 'High', 'color': 'danger', 'description': 'High risk - immediate medical attention recommended'}
    else:
        return {'level': 'Critical', 'color': 'danger', 'description': 'Critical risk - urgent medical intervention required'}

@app.route('/api/info')
def api_info():
    """API endpoint to get model information"""
    if model is None:
        return jsonify({'error': 'Model not loaded'})
    
    return jsonify({
        'model_type': type(model).__name__,
        'features': feature_names,
        'total_features': len(feature_names) if feature_names else 0,
        'status': 'ready'
    })

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    print("🚀 Starting Heart Failure Prediction App...")
    print("📊 Model status:", "✅ Loaded" if model is not None else "❌ Not loaded")
    print("🌐 Access the app at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)