# ❤️ HeartGuard AI - Heart Failure Risk Prediction

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, AI-powered web application for predicting heart failure risk using machine learning. This tool provides healthcare professionals and researchers with an intuitive interface to assess cardiac risk based on clinical parameters.

## 🌟 Features

- **Advanced ML Prediction**: Uses trained machine learning models for accurate risk assessment
- **Beautiful Modern UI**: Professional glass-morphism design with smooth animations
- **Real-time Validation**: Instant form validation with helpful error messages
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Medical-Grade Interface**: Organized by clinical sections with normal value ranges
- **Risk Visualization**: Interactive charts and color-coded risk levels
- **Professional Reports**: Detailed risk assessment with recommendations

## 🚀 Live Demo

![HeartGuard AI Screenshot](/static/images/image.png)

## 📋 Requirements

- Python 3.8+
- Flask 2.3+
- scikit-learn 1.3+
- NumPy 1.24+
- Pandas 2.0+

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/heartguard-ai.git
cd heartguard-ai
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Browser
Navigate to `http://localhost:5000` to access HeartGuard AI.

## 📊 Input Parameters

The application requires the following clinical parameters:

### Personal Information
- **Age**: Patient age in years (1-120)
- **Gender**: Male/Female

### Medical History
- **Anemia**: Presence of anemia (Yes/No)
- **Diabetes**: Diabetes diagnosis (Yes/No)
- **High Blood Pressure**: Hypertension status (Yes/No)
- **Smoking**: Smoking history (Yes/No)

### Clinical Measurements
- **Ejection Fraction**: Left ventricular ejection fraction percentage (10-80%)
- **Follow-up Period**: Days since initial diagnosis (1-365)

### Laboratory Results
- **Creatinine Phosphokinase**: Enzyme level in mcg/L (Normal: 10-120)
- **Platelets**: Platelet count in kiloplatelets/mL (Normal: 150,000-450,000)
- **Serum Creatinine**: Creatinine level in mg/dL (Normal: 0.6-1.2)
- **Serum Sodium**: Sodium level in mEq/L (Normal: 135-145)

## 🎯 Risk Categories

- **🟢 Low Risk (0-20%)**: Continue regular check-ups and healthy lifestyle
- **🟡 Moderate Risk (20-40%)**: Schedule follow-up with cardiologist
- **🟠 High Risk (40-60%)**: Immediate medical consultation recommended
- **🔴 Critical Risk (60%+)**: Urgent medical attention required

## 🏗️ Project Structure

```
heartguard-ai/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── heart_failure_model.pkl     # Trained ML model
├── scaler.pkl                  # Feature scaler (to be generated)
├── feature_names.pkl           # Feature names (to be generated)
├── templates/
│   └── index.html             # Main web interface
├── static/
│   ├── css/
│   │   └── custom.css         # Additional styles
│   ├── js/
│   │   └── custom.js          # Additional JavaScript
│   └── images/
│       └── logo.png           # Application logo
├── screenshots/               # Application screenshots
├── docs/                      # Documentation
├── tests/                     # Unit tests
└── data/                      # Sample data and models
```

## 🧪 Model Information

This application uses a machine learning model trained on heart failure clinical records. The model considers multiple clinical features to predict the probability of mortality events.

### Supported Algorithms
- Random Forest Classifier
- Support Vector Machine (SVM)
- Logistic Regression
- Gradient Boosting Classifier

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
MODEL_PATH=heart_failure_model.pkl
SCALER_PATH=scaler.pkl
```

### Model Configuration
The application automatically detects the model type and applies appropriate preprocessing.

## 📱 API Endpoints

### GET `/`
Returns the main application interface.

### POST `/predict`
Accepts form data and returns risk prediction.

**Request Format:**
```json
{
    "age": 65,
    "anaemia": 0,
    "creatinine_phosphokinase": 582,
    "diabetes": 1,
    "ejection_fraction": 45,
    "high_blood_pressure": 1,
    "platelets": 265000,
    "serum_creatinine": 1.9,
    "serum_sodium": 136,
    "sex": 1,
    "smoking": 0,
    "time": 130
}
```

**Response Format:**
```json
{
    "prediction": 1,
    "death_probability": 75.2,
    "survival_probability": 24.8,
    "risk_level": {
        "level": "High",
        "color": "danger",
        "description": "High risk - immediate medical attention recommended"
    },
    "success": true
}
```

### GET `/api/info`
Returns model information and status.

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Run with coverage:

```bash
python -m pytest tests/ --cov=app --cov-report=html
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

## 🙏 Acknowledgments

- Heart failure dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records)
- Bootstrap 5 for the responsive UI framework
- Font Awesome for icons
- Flask framework for the web application

## 📞 Contact

- **Author**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 📈 Roadmap

- [ ] Add more ML model options
- [ ] Implement user authentication
- [ ] Add data visualization charts
- [ ] Create mobile app version
- [ ] Add multi-language support
- [ ] Implement patient history tracking

---

Made with ❤️ for better healthcare outcomes.
