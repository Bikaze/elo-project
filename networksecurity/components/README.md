# 🧩 ML Components

[![MLOps](https://img.shields.io/badge/MLOps-Pipeline-green?style=for-the-badge)]()
[![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)]()

This directory contains the individual stages of the machine learning lifecycle. Each component is designed to be modular, taking a **Config** object as input and producing an **Artifact** as output.

## ⚙️ The Components

### 1. 📥 Data Ingestion (`data_ingestion.py`)

* **Goal**: Fetch data from the source and prepare it for the pipeline.
* **Source**: MongoDB Atlas.
* **Actions**:
  * Connects to the database.
  * Exports the collection as a DataFrame.
  * Splits data into `train.csv` and `test.csv`.
* **Output**: `DataIngestionArtifact` (paths to train/test files).

### 2. 🛡️ Data Validation (`data_validation.py`)

* **Goal**: Ensure data quality and consistency.
* **Logic**:
  * Checks against `schema.yaml`.
  * Verifies column names and types.
  * Detects data drift (statistical changes in data distribution).
* **Output**: `DataValidationArtifact` (validation status, drift report).

### 3. 🔄 Data Transformation (`data_transformation.py`)

* **Goal**: Prepare raw data for machine learning.
* **Actions**:
  * Imputes missing values (KNN Imputer).
  * Scales numerical features.
  * Saves the `preprocessor.pkl` object for future inference.
* **Output**: `DataTransformationArtifact` (transformed numpy arrays, preprocessor path).

### 4. 🧠 Model Trainer (`model_trainer.py`)

* **Goal**: Train and select the best model.
* **Models Tested**: Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, AdaBoost.
* **Actions**:
  * Trains multiple models.
  * Evaluates them using F1-Score, Precision, and Recall.
  * Selects the best performer.
  * Logs metrics to **MLflow** / **DagsHub**.
* **Output**: `ModelTrainerArtifact` (path to the saved `model.pkl`).

---

<p align="center">
  <a href="../README.md">⬅️ Back to Package README</a>
</p>
