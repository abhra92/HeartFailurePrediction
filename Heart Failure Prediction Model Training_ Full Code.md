
# Heart Failure Prediction Model Training: Full Code and Explanation

This notebook demonstrates how to build and select the best heart failure prediction model using various machine learning algorithms. It includes thorough data analysis, model evaluation, and code formatting suitable for your coursework or deployment.

## 1. Introduction

This notebook covers:

- Data exploration and visualization
- Preparing the dataset
- Training four different machine learning models
- Selecting the best model using accuracy and ROC AUC
- Hyperparameter tuning for the top model
- Model interpretation via feature importance
- Saving the trained model and scaler


## 2. Import Required Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
import pickle
import warnings
warnings.filterwarnings('ignore')
```


## 3. Load the Dataset

```python
# Load the heart failure dataset
df = pd.read_csv('heart_failure_clinical_records_dataset .csv')
```


## 4. Data Overview \& Initial Analysis

```python
print("Dataset Info:")
print(f"Shape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nFirst few rows:")
print(df.head())
```


### Basic Statistics

```python
print("\nDataset Statistics:")
print(df.describe())
```


### Missing Values

```python
print("\nMissing values:")
print(df.isnull().sum())
```


### Target Variable Distribution

```python
print("\nTarget Variable Distribution:")
print(df['DEATH_EVENT'].value_counts())
print(f"Death rate: {df['DEATH_EVENT'].mean():.2%}")
```


## 5. Exploratory Data Analysis (EDA)

```python
plt.figure(figsize=(15, 10))

# Death Event Distribution
plt.subplot(2, 3, 1)
df['DEATH_EVENT'].value_counts().plot(kind='bar')
plt.title('Death Event Distribution')
plt.xlabel('Death Event')
plt.ylabel('Count')

# Age Distribution by Death Event
plt.subplot(2, 3, 2)
plt.hist(df[df['DEATH_EVENT']==0]['age'], alpha=0.7, label='Survived', bins=20)
plt.hist(df[df['DEATH_EVENT']==1]['age'], alpha=0.7, label='Died', bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution by Death Event')
plt.legend()

# Ejection Fraction by Death Event
plt.subplot(2, 3, 3)
plt.hist(df[df['DEATH_EVENT']==0]['ejection_fraction'], alpha=0.7, label='Survived', bins=20)
plt.hist(df[df['DEATH_EVENT']==1]['ejection_fraction'], alpha=0.7, label='Died', bins=20)
plt.xlabel('Ejection Fraction')
plt.ylabel('Frequency')
plt.title('Ejection Fraction by Death Event')
plt.legend()

# Serum Creatinine by Death Event
plt.subplot(2, 3, 4)
plt.hist(df[df['DEATH_EVENT']==0]['serum_creatinine'], alpha=0.7, label='Survived', bins=20)
plt.hist(df[df['DEATH_EVENT']==1]['serum_creatinine'], alpha=0.7, label='Died', bins=20)
plt.xlabel('Serum Creatinine')
plt.ylabel('Frequency')
plt.title('Serum Creatinine by Death Event')
plt.legend()

# Correlation Heatmap
plt.subplot(2, 3, 5)
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f', cbar_kws={"shrink": .8})
plt.title('Feature Correlation Heatmap')

plt.tight_layout()
plt.show()
```

**Explanation:**
This block visualizes the distribution of several key features and their relation to the death event target, helping us identify important patterns in the data.

## 6. Feature Preparation

**Select Features and Target:**

```python
features = [
    'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 
    'ejection_fraction', 'high_blood_pressure', 'platelets', 
    'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time'
]
X = df[features]
y = df['DEATH_EVENT']
```

**Statistics Per Feature:**

```python
print("\nFeature Statistics:")
for feature in features:
    print(f"{feature}: Mean={X[feature].mean():.2f}, Std={X[feature].std():.2f}")
```


## 7. Train-Test Split \& Scaling

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nTraining set shape: {X_train.shape}")
print(f"Test set shape: {X_test.shape}")
```


## 8. Model Initialization

```python
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'SVM': SVC(random_state=42, probability=True)
}
```


## 9. Model Training, Evaluation, and Selection

```python
model_results = {}

for name, model in models.items():
    print(f"\n{'='*50}\nTraining {name}...")
    # Use scaled data for SVM & Logistic Regression
    if name in ['SVM', 'Logistic Regression']:
        X_train_use, X_test_use = X_train_scaled, X_test_scaled
    else:
        X_train_use, X_test_use = X_train, X_test
    # Train and predict
    model.fit(X_train_use, y_train)
    y_pred = model.predict(X_test_use)
    y_pred_proba = model.predict_proba(X_test_use)[:, 1]
    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    cv_scores = cross_val_score(model, X_train_use, y_train, cv=5, scoring='accuracy')
    model_results[name] = {
        'model': model,
        'accuracy': accuracy,
        'roc_auc': roc_auc,
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'y_pred': y_pred,
        'y_pred_proba': y_pred_proba
    }
    print(f"Test Accuracy: {accuracy:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")
    print(f"CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
```


## 10. Select the Best Model

```python
best_model_name = max(model_results.keys(), key=lambda x: model_results[x]['accuracy'])
best_model = model_results[best_model_name]['model']

print(f"\n{'='*50}\nBEST MODEL: {best_model_name}")
print(f"Test Accuracy: {model_results[best_model_name]['accuracy']:.4f}")
print(f"ROC AUC: {model_results[best_model_name]['roc_auc']:.4f}")
```


## 11. Hyperparameter Tuning

```python
if best_model_name == 'Random Forest':
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }
    grid_search = GridSearchCV(
        RandomForestClassifier(random_state=42), param_grid,
        cv=5, scoring='accuracy', n_jobs=-1
    )
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    y_pred_final = best_model.predict(X_test)
    final_accuracy = accuracy_score(y_test, y_pred_final)
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Improved accuracy: {final_accuracy:.4f}")

elif best_model_name == 'Gradient Boosting':
    param_grid = {
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 7]
    }
    grid_search = GridSearchCV(
        GradientBoostingClassifier(random_state=42), param_grid,
        cv=5, scoring='accuracy', n_jobs=-1
    )
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    y_pred_final = best_model.predict(X_test)
    final_accuracy = accuracy_score(y_test, y_pred_final)
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Improved accuracy: {final_accuracy:.4f}")
```


## 12. Feature Importance

```python
if hasattr(best_model, 'feature_importances_'):
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': best_model.feature_importances_
    }).sort_values('importance', ascending=False)
    print("\nFeature Importance:")
    print(feature_importance)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=feature_importance.head(10), x='importance', y='feature')
    plt.title('Top 10 Feature Importance')
    plt.xlabel('Importance')
    plt.tight_layout()
    plt.show()
```

**Explanation:**
This plot and table highlight the features most important for prediction according to the best tree-based model.

## 13. Final Model Evaluation (Confusion Matrix)

```python
print(f"\n{'='*50}\nFINAL MODEL EVALUATION\nModel: {best_model_name}")

if 'final_accuracy' in locals():
    print(f"Final Test Accuracy: {final_accuracy:.4f}")
    final_pred = y_pred_final
else:
    final_accuracy = model_results[best_model_name]['accuracy']
    print(f"Final Test Accuracy: {final_accuracy:.4f}")
    final_pred = model_results[best_model_name]['y_pred']

cm = confusion_matrix(y_test, final_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Survived', 'Died'], yticklabels=['Survived', 'Died'])
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()
```


## 14. Save Trained Model and Artifacts

```python
print("\nSaving model and scaler...")

with open('heart_failure_model.pkl', 'wb') as f:
    pickle.dump(best_model, f)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('feature_names.pkl', 'wb') as f:
    pickle.dump(features, f)

print("Model saved as 'heart_failure_model.pkl'")
print("Scaler saved as 'scaler.pkl'")
print("Feature names saved as 'feature_names.pkl'")
```


## 15. Model Summary and Accuracy

```python
print(f"\n{'='*50}\nMODEL SUMMARY")
print(f"Best Model: {best_model_name}")
print(f"Final Accuracy: {final_accuracy:.4f} ({final_accuracy*100:.2f}%)")
print("Model saved and ready for deployment!")

if final_accuracy >= 0.80:
    print("✅ SUCCESS: Accuracy target of 80%+ achieved!")
else:
    print(f"⚠️  Note: Accuracy is {final_accuracy*100:.2f}%, target was 80%+")
```


## 16. Explanation

- **Exploratory Visualizations** show patterns between patient characteristics and survival.
- **Feature Scaling** is critical for algorithms like Logistic Regression and SVM.
- **Multiple Algorithms** are compared using accuracy, ROC AUC, and 5-fold cross-validation.
- **Tree-based Models** (Random Forest, Gradient Boosting) provide feature importance for interpretability.
- **Hyperparameter Tuning** with GridSearchCV squeezes the best out of the top model.
- **Model and Scaler Saving** allows for reliable and consistent inference in the future.


## 17. How to Use This Notebook

- Replace `'heart_failure_clinical_records_dataset .csv'` with your dataset path if needed.
- Run each cell top-down in a Jupyter environment (.ipynb) for seamless code + output.
- Extend or modify visualizations or models as required for your coursework or research purposes.

**Ready for deployment! You may now use the `.pkl` files in server APIs or applications for real-time patient prediction.**

