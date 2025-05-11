<<<<<<< HEAD
# Customer Satisfaction Prediction - End-to-End Pipelines with ZenML & MLflow

![pipeline zenml and mlflow](https://github.com/user-attachments/assets/4ed70ce3-183c-43c3-b118-08b6238379fc)


## 📌 Project Overview
This project is focused on building and deploying an end-to-end machine learning pipeline for **Customer Satisfaction Prediction** using **ZenML** and **MLflow**. It covers:

- **Data Ingestion & Processing**
- **Model Training & Evaluation**
- **Experiment Tracking with MLflow**
- **Pipeline Orchestration using ZenML**

---

## 🚀 Setup Instructions

### **Prerequisites**
Ensure you have **Python 3.8+** installed, then install the required dependencies:

```bash
pip install zenml mlflow
```

### **ZenML & MLflow Integration**
Install and configure MLflow with ZenML:
=======

## Steps to Achieve a Production-Level Project

### Required Files for Building Pipelines Successfully

#### Create a Folder Named "src" for Source Files
1. `__init__.py` - Initializes the folder as a Python package.
2. `data_config.py` - Contains configuration settings for data processing.
3. `data_cleaning.py` - Scripts for cleaning and preprocessing data.
4. `model_dev.py` - Code for model development and training.
5. `evaluation.py` - Functions for evaluating model performance.

#### Create a "steps" Folder for Pipeline Operations
1. `ingest_data.py` - Handles data ingestion.
2. `data_clean.py` - Manages data cleaning steps.
3. `train_model.py` - Script to train the model.
4. `evaluate.py` - Evaluates the trained model.
5. `config.py` - Configuration file for model parameters.

#### Create a Pipeline Orchestration Folder
1. `pipeline_training.py` - Orchestrates the training pipeline.

#### Separate Python Files to Orchestrate All Files
1. `__init__.py` - Initializes the folder as a Python package (should be empty but necessary).
2. `run_pipeline.py` - Runs the pipeline, inheriting from `pipeline_training.py`.
3. `requirements.txt` - Lists all dependencies required for the project.
    ```
    catboost==1.2.7
    joblib==1.4.2
    lightgbm==4.5.0
    optuna==2.10.1
    streamlit==1.9.0
    xgboost==1.6.0
    markupsafe==2.1.1
    zenml
    numpy
    pandas
    scikit-learn
    ```

### Running the Pipeline
To run the pipeline, use the following command:
```sh
python run_pipeline.py
```

### Monitoring ZenML Pipeline Locally
To monitor the ZenML pipeline locally, use this command:
```sh
zenml login --local --blocking
```

### Disconnecting Locally
To disconnect locally, use this command:
```sh
zenml disconnect
```

### Shutting Down the ZenML Pipeline
To shut down the ZenML pipeline, use this command:
```sh
zenml down
```
#for describe use this command 
```sh
zenml stack describe
```
ZenML Project Setup for Local Development with MLflow and Seldon Deployer
This guide provides a step-by-step approach to setting up a ZenML project for local development with MLflow integration and Seldon model deployment.

Table of Contents
Introduction

Installation

Initialization

Registering Stack Components

Artifact Store

Orchestrator

Experiment Tracker

Model Deployer

Creating and Registering a Stack

Setting the Default Stack

Verifying the Setup

Example Pipeline

Launching the MLflow UI

Conclusion

Introduction
This project demonstrates how to set up a local development environment using ZenML with MLflow integration and Seldon model deployment. It provides a complete workflow to train machine learning models, track experiments, and deploy models locally.

Installation
First, install the necessary packages:

bash
pip install zenml
pip install mlflow
pip install seldon-core
Initialization
Create a ZenML repository in your project directory:

bash
zenml init
This command initializes a new ZenML repository, setting up the necessary structure for your project.

Registering Stack Components
ZenML requires you to register various components that it uses for different stages of the machine learning lifecycle.

# MLflow with ZenML - Setup & Troubleshooting Guide

## 🚀 Prerequisites

Before running MLflow with ZenML, ensure you have:

- Python installed (Recommended: 3.8+)
- ZenML installed (`pip install zenml`)
- MLflow installed (`pip install mlflow`)
- A properly configured ZenML stack

## 🔧 Step 1: Install & Integrate MLflow with ZenML
>>>>>>> d723c8c74 (Initial project upload)

```bash
zenml integration install mlflow -y
```

<<<<<<< HEAD
### **Register and Configure ZenML Stack**
=======
## 🛠 Step 2: Register MLflow Components in ZenML
>>>>>>> d723c8c74 (Initial project upload)

```bash
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow --flavor=mlflow
zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set
```

<<<<<<< HEAD
---

## 📂 Project Structure

```
PROJECT-1/
├── pipelines/
│   ├── __pycache__/
│   ├── data/
│   │   └── olist_customers_dataset.csv
│   ├── deployement_pipeline.py
│   └── training_pipeline.py
├── src/
│   ├── __pycache__/
│   ├── utils/
│   │   ├── __pycache__/
│   │   ├── artifacts_store.py
│   │   ├── __init__.py
│   │   ├── data_cleaning.py
│   │   ├── data_config.py
│   │   ├── evaluation.py
│   │   └── model_dev.py
├── steps/
│   ├── clean_data.py
│   ├── config.py
│   ├── evaluation.py
│   ├── ingest_data.py
│   ├── model_train.py
│   └── __init__.py
├── .gitignore
├── requirements.txt
├── run_deployement.py
└── run_pipeline.py

```

---

## ⚡ Running the Pipeline
Run the training pipeline using:
=======
## 🚀 Step 3: Run Your ZenML Pipeline
>>>>>>> d723c8c74 (Initial project upload)

```bash
python run_pipeline.py
```

![Screenshot 2025-02-11 224101](https://github.com/user-attachments/assets/0accfc7d-2916-46de-82c8-42053aa77ca8)




<<<<<<< HEAD
Expected output:

```
Initiating a new run for the pipeline: train_pipeline.
Using stack: mlflow_stack
=======
After running, it should output something like:

```
Initiating a new run for the pipeline: train_pipeline.
Using user: default
Using stack: mlflow_stack
  orchestrator: default
  artifact_store: default
>>>>>>> d723c8c74 (Initial project upload)
  experiment_tracker: mlflow_tracker
  model_deployer: mlflow
```

<<<<<<< HEAD
---

## 📊 MLflow UI Interactions

To visualize experiment tracking, start the MLflow UI:

```bash
mlflow ui --backend-store-uri "file:C:\Users\seerl\AppData\Roaming\zenml\local_stores\<your_local_store_id>\mlruns"
```

Then, open your browser and visit:
=======
## 📊 Step 4: Start the MLflow UI

To visualize experiments and logged runs:

```bash
mlflow ui --backend-store-uri "file:C:\Users\seerl\AppData\Roaming\zenml\local_stores\4166d845-32b2-4327-8958-7d66d0d4d649\mlruns"
```

Then, open your browser and go to:
>>>>>>> d723c8c74 (Initial project upload)

```
http://127.0.0.1:5000
```

<<<<<<< HEAD
---

## 🛠 ZenML Server Operations

### **Start ZenML UI (Pipelines Dashboard)**

```bash
zenml up
```

> ⚠️ **Note:** If `zenml up` is not working, try running it with `--local --blocking` (currently not functioning correctly).

### **Shut Down ZenML**

```bash
zenml down
```

---

## 🎯 Conclusion
You have successfully set up an **end-to-end machine learning pipeline** with **ZenML & MLflow**! 🚀🔥

For troubleshooting, check the logs or restart services. Happy coding! 😎
=======
## 🔍 Troubleshooting

### ✅ MLflow UI is empty

1. Ensure your pipeline ran successfully and logs exist:
   ```bash
   ls C:\Users\seerl\AppData\Roaming\zenml\local_stores\4166d845-32b2-4327-8958-7d66d0d4d649\mlruns
   ```
   If it's empty, rerun the pipeline.
2. Make sure you're pointing to the correct backend store.
3. Restart the MLflow UI and clear the browser cache.

### ⚠️ Pydantic Model Name Warning

If you see:

```
Field "model_name" has conflict with protected namespace "model_".
```

Fix it by adding this to your Pydantic model:

```python
class MyModel(BaseModel):
    model_name: str
    model_config = {'protected_namespaces': ()}
```

## 🎯 Conclusion

You’re now all set up to track experiments with ZenML and MLflow! 🚀🔥




>>>>>>> d723c8c74 (Initial project upload)

