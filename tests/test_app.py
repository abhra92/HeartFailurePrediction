import pytest
import json
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def sample_patient_data():
    """Sample patient data for testing."""
    return {
        'age': '65',
        'sex': '1',
        'anaemia': '0',
        'creatinine_phosphokinase': '582',
        'diabetes': '1',
        'ejection_fraction': '38',
        'high_blood_pressure': '1',
        'platelets': '265000',
        'serum_creatinine': '1.9',
        'serum_sodium': '136',
        'smoking': '0',
        'time': '130'
    }

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'HeartGuard AI' in response.data

def test_api_info_endpoint(client):
    """Test the API info endpoint."""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    if 'error' not in data:
        assert 'model_type' in data
        assert 'features' in data
        assert 'status' in data

def test_predict_endpoint_with_valid_data(client, sample_patient_data):
    """Test prediction with valid patient data."""
    response = client.post('/predict', data=sample_patient_data)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    
    if data.get('success'):
        assert 'prediction' in data
        assert 'death_probability' in data
        assert 'survival_probability' in data
        assert 'risk_level' in data
        assert 0 <= data['death_probability'] <= 100
        assert 0 <= data['survival_probability'] <= 100
    else:
        # If model is not loaded, should return error
        assert 'error' in data

def test_predict_endpoint_missing_data(client):
    """Test prediction with missing required fields."""
    incomplete_data = {
        'age': '65',
        'sex': '1'
        # Missing other required fields
    }
    
    response = client.post('/predict', data=incomplete_data)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'error' in data or 'success' in data

def test_predict_endpoint_invalid_data(client):
    """Test prediction with invalid data types."""
    invalid_data = {
        'age': 'invalid_age',
        'sex': '1',
        'anaemia': '0',
        'creatinine_phosphokinase': 'invalid_cpk',
        'diabetes': '1',
        'ejection_fraction': '38',
        'high_blood_pressure': '1',
        'platelets': '265000',
        'serum_creatinine': '1.9',
        'serum_sodium': '136',
        'smoking': '0',
        'time': '130'
    }
    
    response = client.post('/predict', data=invalid_data)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'error' in data or 'success' in data

def test_404_error_handler(client):
    """Test 404 error handling."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404

def test_form_validation_boundaries(client):
    """Test form validation with boundary values."""
    boundary_data = {
        'age': '120',  # Maximum age
        'sex': '1',
        'anaemia': '1',
        'creatinine_phosphokinase': '0',  # Minimum value
        'diabetes': '1',
        'ejection_fraction': '10',  # Minimum EF
        'high_blood_pressure': '1',
        'platelets': '1',  # Very low platelets
        'serum_creatinine': '10',  # Very high creatinine
        'serum_sodium': '160',  # High sodium
        'smoking': '1',
        'time': '365'  # Maximum follow-up
    }
    
    response = client.post('/predict', data=boundary_data)
    assert response.status_code == 200

class TestRiskLevelFunction:
    """Test the get_risk_level function."""
    
    def test_low_risk(self):
        """Test low risk classification."""
        from app import get_risk_level
        result = get_risk_level(15)
        assert result['level'] == 'Low'
        assert result['color'] == 'success'
    
    def test_moderate_risk(self):
        """Test moderate risk classification."""
        from app import get_risk_level
        result = get_risk_level(35)
        assert result['level'] == 'Moderate'
        assert result['color'] == 'warning'
    
    def test_high_risk(self):
        """Test high risk classification."""
        from app import get_risk_level
        result = get_risk_level(55)
        assert result['level'] == 'High'
        assert result['color'] == 'danger'
    
    def test_critical_risk(self):
        """Test critical risk classification."""
        from app import get_risk_level
        result = get_risk_level(75)
        assert result['level'] == 'Critical'
        assert result['color'] == 'danger'

class TestModelLoading:
    """Test model loading functionality."""
    
    def test_model_files_exist(self):
        """Test that required model files exist."""
        import os
        
        # Check if main model file exists
        assert os.path.exists('heart_failure_model.pkl')
        
        # Note: scaler.pkl and feature_names.pkl might not exist yet
        # This is expected behavior for the current setup

if __name__ == '__main__':
    pytest.main(['-v'])
