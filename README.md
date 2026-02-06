# Well Monitoring System – PyQt, AI Model, and FastAPI Deployment

This project is divided into four main parts covering the desktop interface, AI modeling, deployment, and API integration. The system focuses on monitoring well conditions using sensor data and predicting the well status through a trained machine learning model.

---

## Project Structure

```
├── pyqt_draw/
├── AI/
│   ├── 3w_dataset_part1.ipynb
│   ├── 3w_dataset_part2.ipynb
│   └── cleaned_final_dataset.csv
├── deployment/
│   ├── main.py
│   ├── model.joblib
│   └── requirements.txt
├── interface/
│   ├── main.py
│   ├── config.py
│   └── api_client.py
```

Folder: `pyqt_draw`

This folder contains all components related to the PyQt drawing application.  
It includes the UI logic, drawing features, and desktop interface implementation.

---

## Part 2 — AI Model

The AI module was developed using the **3W Dataset**.

Dataset Link (Kaggle):  
https://www.kaggle.com/datasets/afrniomelo/3w-dataset

Full AI Documentation (Google Drive):  
https://drive.google.com/file/d/1Z7zIXH2XHsD9822ax5IckkWMh1rhhbrS/view?usp=sharing

The documentation explains:

- Dataset selection
- Preprocessing steps
- Model training
- Evaluation and results

---

## Part 3 — Deployment (FastAPI)

The deployment layer uses **FastAPI** to serve the trained model as an API.

### Description

- The saved model file (`.joblib`) receives five sensor values.
- The API returns the predicted well condition.

### Required Files

- `model.joblib` — trained machine learning model
- `requirements.txt` — libraries with exact versions used during training
- `main.py` — FastAPI application entry point

### How to Run

Open the terminal inside the deployment directory and run: uvicorn main:app --reload

---

## Part 4 — Interface Integration

Folder: `interface`

This folder contains:

- **main file**: The user interface for entering sensor values.
- **config**: Stores the API endpoint configuration.
- **api_client**: Includes functions responsible for:
  - Sending sensor data to the API
  - Receiving and displaying prediction results

---

## Overview

The system workflow is as follows:

1. The interface collects five sensor readings.
2. Data is sent through the FastAPI endpoint.
3. The trained AI model processes the input.
4. The API returns the predicted well status to the interface.

---

## Technologies Used

- Python
- PyQt
- Machine Learning
- FastAPI
- Joblib
- REST API Integration

---

