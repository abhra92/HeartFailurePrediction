# HeartGuard AI - Installation Guide

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB free space
- **Internet**: Required for initial setup and dependencies

### Recommended Requirements
- **Python**: Version 3.9 or 3.10
- **RAM**: 8GB or more
- **Storage**: 1GB free space
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, or Edge 90+

## Installation Methods

### Method 1: Quick Installation (Recommended)

1. **Download the Project**
   ```bash
   git clone https://github.com/yourusername/heartguard-ai.git
   cd heartguard-ai
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - **Windows:**
     ```cmd
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   Open your browser and navigate to: `http://localhost:5000`

### Method 2: Development Installation

For developers who want to contribute or modify the code:

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/heartguard-ai.git
   cd heartguard-ai
   ```

2. **Create Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Additional dev dependencies
   ```

3. **Set Environment Variables**
   Create a `.env` file:
   ```env
   FLASK_ENV=development
   FLASK_DEBUG=True
   SECRET_KEY=your-development-secret-key
   ```

4. **Run in Development Mode**
   ```bash
   flask run --debug
   ```

### Method 3: Docker Installation

If you prefer using Docker:

1. **Build Docker Image**
   ```bash
   docker build -t heartguard-ai .
   ```

2. **Run Container**
   ```bash
   docker run -p 5000:5000 heartguard-ai
   ```

## Troubleshooting

### Common Issues

#### Python Version Issues
```bash
# Check Python version
python --version

# If you have multiple Python versions, use specific version
python3.9 -m venv venv
```

#### Package Installation Errors
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install packages individually if batch install fails
pip install flask
pip install numpy
pip install pandas
pip install scikit-learn
```

#### Port Already in Use
```bash
# Run on different port
python app.py --port 5001
```

#### Permission Errors (Linux/macOS)
```bash
# Use --user flag
pip install --user -r requirements.txt
```

### Windows-Specific Issues

#### PowerShell Execution Policy
```powershell
# If you get execution policy errors
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Missing Visual C++ Build Tools
Download and install Microsoft Visual C++ Build Tools from the official Microsoft website.

### macOS-Specific Issues

#### Xcode Command Line Tools
```bash
xcode-select --install
```

#### Homebrew Python
```bash
# If using Homebrew Python
brew install python@3.9
python3.9 -m venv venv
```

### Linux-Specific Issues

#### Missing System Dependencies
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-venv

# CentOS/RHEL
sudo yum install python3-devel python3-pip
```

## Verification

After installation, verify everything works:

1. **Check Dependencies**
   ```bash
   pip list
   ```

2. **Test Import**
   ```python
   python -c "import flask, numpy, pandas, sklearn; print('All dependencies imported successfully')"
   ```

3. **Test Application**
   - Navigate to `http://localhost:5000`
   - Fill out the form with test data
   - Verify prediction results appear

## Performance Optimization

### For Production Deployment

1. **Use Production WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Enable Caching**
   ```python
   # Add to app.py
   from flask_caching import Cache
   cache = Cache(app, config={'CACHE_TYPE': 'simple'})
   ```

3. **Configure Reverse Proxy**
   Use nginx or Apache as a reverse proxy for better performance.

## Next Steps

After successful installation:

1. Read the [User Guide](user-guide.md)
2. Explore the [API Documentation](api-documentation.md)
3. Check out [Configuration Options](configuration.md)
4. Learn about [Model Details](model-documentation.md)

## Getting Help

If you encounter issues:

1. Check the [FAQ](faq.md)
2. Search existing [GitHub Issues](https://github.com/yourusername/heartguard-ai/issues)
3. Create a new issue with:
   - Your operating system
   - Python version
   - Error messages (full traceback)
   - Steps to reproduce

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for development setup and contribution guidelines.
