# Contributing to HeartGuard AI

First off, thank you for considering contributing to HeartGuard AI! It's people like you that make this project a great tool for healthcare assessment.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what behavior you expected to see**
- **Include screenshots if applicable**
- **Include your environment details** (OS, Python version, browser, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and explain which behavior you expected to see**
- **Explain why this enhancement would be useful**

### Your First Code Contribution

Unsure where to begin contributing? You can start by looking through these beginner-friendly issues:

- **good-first-issue** - issues which should only require a few lines of code
- **help-wanted** - issues which should be a bit more involved than beginner issues

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- Text editor or IDE

### Setting Up Development Environment

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/heartguard-ai.git
   cd heartguard-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=app --cov-report=html

# Run specific test file
python -m pytest tests/test_app.py

# Run with verbose output
python -m pytest -v
```

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

Run all checks:
```bash
# Format code
black .
isort .

# Check linting
flake8

# Type checking
mypy app.py
```

### Running the Application

```bash
# Development mode
flask run --debug

# Or directly
python app.py
```

## Project Structure

```
heartguard-ai/
├── app.py                 # Main Flask application
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── templates/
│   └── index.html        # Main template
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── tests/                # Test files
├── docs/                 # Documentation
├── .github/              # GitHub workflows
└── scripts/              # Utility scripts
```

## Coding Guidelines

### Python Code

- Follow PEP 8 style guide
- Use type hints where possible
- Write docstrings for functions and classes
- Keep functions small and focused
- Use meaningful variable and function names

Example:
```python
def predict_heart_failure_risk(
    age: int,
    ejection_fraction: float,
    serum_creatinine: float
) -> Dict[str, Any]:
    """
    Predict heart failure risk based on patient data.
    
    Args:
        age: Patient age in years
        ejection_fraction: Left ventricular ejection fraction (%)
        serum_creatinine: Serum creatinine level (mg/dL)
    
    Returns:
        Dictionary containing prediction results
    """
    # Implementation here
    pass
```

### HTML/CSS

- Use semantic HTML5 elements
- Follow accessibility guidelines (WCAG 2.1)
- Use Bootstrap classes when possible
- Keep CSS organized and commented
- Use CSS custom properties for theming

### JavaScript

- Use modern ES6+ syntax
- Follow ESLint rules
- Write JSDoc comments for functions
- Use async/await for asynchronous operations
- Handle errors gracefully

## Testing Guidelines

### Unit Tests

- Write tests for all new functions
- Test both success and failure cases
- Use descriptive test names
- Mock external dependencies

Example:
```python
def test_predict_heart_failure_risk_high_risk():
    """Test prediction for high-risk patient."""
    result = predict_heart_failure_risk(
        age=75,
        ejection_fraction=25,
        serum_creatinine=2.5
    )
    assert result['risk_level'] == 'High'
    assert result['death_probability'] > 60
```

### Integration Tests

- Test complete user workflows
- Test API endpoints
- Test form validation
- Test error handling

### Browser Testing

Test the UI in:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Documentation

### Code Documentation

- Write clear docstrings
- Include type hints
- Add inline comments for complex logic
- Update API documentation

### User Documentation

- Update README.md for new features
- Add examples for new functionality
- Keep installation instructions current
- Document configuration options

## Release Process

1. Update version numbers
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Deploy to production

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- CONTRIBUTORS.md file

## Questions?

Don't hesitate to reach out:
- Open an issue for questions about the project
- Join our discussions on GitHub
- Contact maintainers directly

Thank you for contributing to HeartGuard AI! 🚀
