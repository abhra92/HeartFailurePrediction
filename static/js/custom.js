// Custom JavaScript for HeartGuard AI

class HeartGuardAI {
    constructor() {
        this.init();
    }

    init() {
        this.setupAnalytics();
        this.setupKeyboardShortcuts();
        this.setupAccessibility();
        this.setupDataExport();
    }

    setupAnalytics() {
        // Track form interactions
        document.getElementById('prediction-form').addEventListener('submit', () => {
            this.trackEvent('prediction_submitted', {
                timestamp: new Date().toISOString()
            });
        });
    }

    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Alt + P to focus on predict button
            if (e.altKey && e.key === 'p') {
                e.preventDefault();
                document.getElementById('predict-button').focus();
            }
            
            // Ctrl + R to reset form
            if (e.ctrlKey && e.key === 'r') {
                e.preventDefault();
                this.resetForm();
            }
        });
    }

    setupAccessibility() {
        // Add ARIA labels and descriptions
        const form = document.getElementById('prediction-form');
        form.setAttribute('aria-label', 'Heart failure risk assessment form');
        
        // Add live region for dynamic updates
        const liveRegion = document.createElement('div');
        liveRegion.setAttribute('aria-live', 'polite');
        liveRegion.setAttribute('aria-atomic', 'true');
        liveRegion.className = 'sr-only';
        liveRegion.id = 'live-region';
        document.body.appendChild(liveRegion);
    }

    setupDataExport() {
        // Add export functionality
        const exportBtn = document.createElement('button');
        exportBtn.className = 'btn btn-outline-secondary btn-sm ms-2';
        exportBtn.innerHTML = '<i class="fas fa-download me-1"></i>Export';
        exportBtn.onclick = () => this.exportResults();
        
        // Add to result card when it becomes visible
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.target.id === 'result-card' && 
                    mutation.target.style.display !== 'none') {
                    const resultHeader = mutation.target.querySelector('h2');
                    if (resultHeader && !document.getElementById('export-btn')) {
                        exportBtn.id = 'export-btn';
                        resultHeader.appendChild(exportBtn);
                    }
                }
            });
        });
        
        observer.observe(document.getElementById('result-card'), {
            attributes: true,
            attributeFilter: ['style']
        });
    }

    resetForm() {
        document.getElementById('prediction-form').reset();
        document.getElementById('result-card').style.display = 'none';
        
        // Reset validation states
        const inputs = document.querySelectorAll('.form-control, .form-select');
        inputs.forEach(input => {
            input.classList.remove('is-valid', 'is-invalid');
        });
        
        this.announceToScreenReader('Form has been reset');
    }

    exportResults() {
        const resultData = this.extractResultData();
        const jsonData = JSON.stringify(resultData, null, 2);
        
        const blob = new Blob([jsonData], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = `heart-failure-assessment-${new Date().toISOString().split('T')[0]}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        
        URL.revokeObjectURL(url);
        this.announceToScreenReader('Results exported successfully');
    }

    extractResultData() {
        const formData = new FormData(document.getElementById('prediction-form'));
        const inputs = {};
        for (let [key, value] of formData.entries()) {
            inputs[key] = value;
        }
        
        const riskLevel = document.getElementById('risk-level')?.textContent || '';
        const riskPercentage = document.getElementById('risk-percentage')?.textContent || '';
        const riskDescription = document.getElementById('risk-description')?.textContent || '';
        
        return {
            timestamp: new Date().toISOString(),
            inputs: inputs,
            results: {
                riskLevel: riskLevel,
                riskPercentage: riskPercentage,
                description: riskDescription
            },
            metadata: {
                version: '1.0.0',
                model: 'HeartGuard AI'
            }
        };
    }

    trackEvent(eventName, data = {}) {
        // Simple event tracking (can be extended with analytics services)
        console.log(`Event: ${eventName}`, data);
        
        // Store in localStorage for debugging
        const events = JSON.parse(localStorage.getItem('heartguard_events') || '[]');
        events.push({
            event: eventName,
            data: data,
            timestamp: new Date().toISOString()
        });
        localStorage.setItem('heartguard_events', JSON.stringify(events.slice(-100))); // Keep last 100 events
    }

    announceToScreenReader(message) {
        const liveRegion = document.getElementById('live-region');
        if (liveRegion) {
            liveRegion.textContent = message;
        }
    }

    // Utility method for form validation
    static validateInput(input, rules = {}) {
        const value = parseFloat(input.value);
        const { min, max, required } = rules;
        
        if (required && !input.value) {
            return { valid: false, message: 'This field is required' };
        }
        
        if (min !== undefined && value < min) {
            return { valid: false, message: `Value must be at least ${min}` };
        }
        
        if (max !== undefined && value > max) {
            return { valid: false, message: `Value must be at most ${max}` };
        }
        
        return { valid: true, message: '' };
    }

    // Method to format numbers for display
    static formatNumber(num, decimals = 1) {
        return Number(num).toFixed(decimals);
    }

    // Method to generate random patient data for testing
    generateTestData() {
        const testData = {
            age: Math.floor(Math.random() * 40) + 40, // 40-80
            sex: Math.floor(Math.random() * 2), // 0-1
            anaemia: Math.floor(Math.random() * 2), // 0-1
            diabetes: Math.floor(Math.random() * 2), // 0-1
            high_blood_pressure: Math.floor(Math.random() * 2), // 0-1
            smoking: Math.floor(Math.random() * 2), // 0-1
            ejection_fraction: Math.floor(Math.random() * 40) + 20, // 20-60
            time: Math.floor(Math.random() * 200) + 30, // 30-230
            creatinine_phosphokinase: Math.floor(Math.random() * 1000) + 100, // 100-1100
            platelets: Math.floor(Math.random() * 300000) + 150000, // 150k-450k
            serum_creatinine: (Math.random() * 2 + 0.5).toFixed(2), // 0.5-2.5
            serum_sodium: Math.floor(Math.random() * 20) + 125 // 125-145
        };
        
        // Fill form with test data
        Object.keys(testData).forEach(key => {
            const input = document.getElementById(key);
            if (input) {
                input.value = testData[key];
                input.dispatchEvent(new Event('input'));
            }
        });
        
        this.announceToScreenReader('Test data populated in form');
        return testData;
    }
}

// Initialize HeartGuard AI when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.heartGuardAI = new HeartGuardAI();
    
    // Add keyboard shortcut help
    console.log(`
    🚀 HeartGuard AI Keyboard Shortcuts:
    Alt + P: Focus predict button
    Ctrl + R: Reset form
    
    💡 Developer Commands:
    heartGuardAI.generateTestData() - Fill form with test data
    heartGuardAI.exportResults() - Export current results
    heartGuardAI.resetForm() - Reset the form
    `);
});

// PWA Service Worker Registration (if available)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then((registration) => {
                console.log('SW registered: ', registration);
            })
            .catch((registrationError) => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
