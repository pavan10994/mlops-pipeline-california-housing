# 🏡 End-to-End California Housing MLOps Pipeline

[![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=flat&logo=mlflow&logoColor=white)](https://mlflow.org/)
[![DagsHub](https://img.shields.io/badge/DagsHub-Repository-000000?style=flat&logo=dagshub&logoColor=white)](https://dagshub.com/)
[![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=flat&logo=render&logoColor=white)](https://render.com/)

An end-to-end, production-grade MLOps pipeline built from scratch to predict California housing prices. The project features modular Python packaging, automated schema data validation, remote experiment tracking with MLflow on DagsHub, containerization via Docker, and live cloud deployment on Render.

🚀 **Live Web App:** [https://mlops-pipeline-california-housing.onrender.com](https://mlops-pipeline-california-housing.onrender.com)  
📊 **DagsHub / MLflow Experiments:** [https://dagshub.com/pavan10994/mlops-pipeline-california-housing](https://dagshub.com/pavan10994/mlops-pipeline-california-housing)

---

## 🛠️ Complete Tech Stack & Tools

| Layer | Tool / Tech Used | Purpose |
| :--- | :--- | :--- |
| **Language & Environment** | Python 3.10 | Modular OOP structure, `setup.py` editable packaging |
| **Pipeline Utilities** | `python-box`, `ensure`, `PyYAML` | Type enforcement & configuration parsing via `ConfigBox` |
| **Data Processing & ML** | Pandas, NumPy, Scikit-Learn | Data transformation & ElasticNet Regression model training |
| **Experiment Tracking** | MLflow | Remote metric logging ($RMSE, MAE, R^2$) & hyperparameter tracking |
| **Remote Registry & Hosting**| DagsHub | Remote storage for MLflow experiments & model registry |
| **Web Framework & UI** | Flask, HTML5, Bootstrap 5 | Interactive web application for user inputs & price inference |
| **Containerization** | Docker | Creating identical, lightweight environment images |
| **Version Control & CI/CD** | Git, GitHub | Distributed version control & repository management |
| **Cloud Deployment** | Render | Continuous automated container hosting & web deployment |

---

## 📐 Pipeline Architecture

```text
               ┌────────────────────────┐
               │    1. Data Ingestion   │
               └───────────┬────────────┘
                           ▼
               ┌────────────────────────┐
               │   2. Data Validation   │ ──(Fails)──► [Halt Pipeline]
               └───────────┬────────────┘
                           │ (Passes)
                           ▼
               ┌────────────────────────┐
               │ 3. Data Transformation │
               └───────────┬────────────┘
                           ▼
               ┌────────────────────────┐
               │    4. Model Training   │
               └───────────┬────────────┘
                           ▼
               ┌────────────────────────┐
               │  5. Model Evaluation   │ ──► [Log Metrics & Model to MLflow/DagsHub]
               └───────────┬────────────┘
                           ▼
               ┌────────────────────────┐
               │  6. Flask Web Service  │
               └───────────┬────────────┘
                           ▼
               ┌────────────────────────┐
               │  7. Docker Container   │ ──► [Deploy to Render Platform]
               └───────────┘
```

---

## 📂 Project Directory Structure

```text
mlops-pipeline-california-housing/
├── .github/
│   └── workflows/          # CI/CD automation workflows
├── artifacts/              # Generated pipeline outputs (data, models, metrics)
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
├── config/
│   └── config.yaml         # Project configuration file paths
├── logs/
│   └── running_logs.log    # Centralized system log output
├── research/
│   └── trials.ipynb        # Exploratory Jupyter Notebooks
├── src/
│   └── mlProject/
│       ├── __init__.py     # Package initialization and logging setup
│       ├── components/     # Ingestion, Validation, Transformation, Trainer, Evaluation
│       ├── config/         # Configuration Manager class definition
│       ├── constants/      # Static path variables
│       ├── entity/         # Dataclass entity configurations
│       ├── pipeline/       # Executable pipeline stage files
│       └── utils/          # Universal helper functions (YAML/JSON loaders)
├── templates/
│   └── index.html          # Web application front-end UI
├── app.py                  # Flask web application entry point
├── Dockerfile              # Docker container instructions
├── main.py                 # Pipeline orchestrator entry point
├── params.yaml             # Model hyperparameter values
├── schema.yaml             # Schema validation and dataset rules
├── requirements.txt        # Production dependencies
├── setup.py                # Local package setup configuration
└── README.md               # Project documentation
```

---

## 🚀 Local Setup & Execution Guide

### Step 1: Clone Repository & Create Virtual Environment
```bash
git clone [https://github.com/pavan10994/mlops-pipeline-california-housing.git](https://github.com/pavan10994/mlops-pipeline-california-housing.git)
cd mlops-pipeline-california-housing

python -m venv venv
```

Activate the virtual environment:
* **Windows (PowerShell):** `.\venv\Scripts\activate`
* **Windows (CMD):** `venv\Scripts\activate`
* **Linux/macOS:** `source venv/bin/activate`

### Step 2: Install Project Requirements
```bash
pip install -r requirements.txt
```

### Step 3: Set Up DagsHub Remote Credentials
Export your environment variables so MLflow can send metrics and artifacts directly to DagsHub:

**Windows (PowerShell):**
```powershell
$env:MLFLOW_TRACKING_URI="[https://dagshub.com/pavan10994/mlops-pipeline-california-housing.mlflow](https://dagshub.com/pavan10994/mlops-pipeline-california-housing.mlflow)"
$env:MLFLOW_TRACKING_USERNAME="pavan10994"
$env:MLFLOW_TRACKING_PASSWORD="YOUR_DAGSHUB_TOKEN"
```

**Windows (CMD):**
```cmd
set MLFLOW_TRACKING_URI=[https://dagshub.com/pavan10994/mlops-pipeline-california-housing.mlflow](https://dagshub.com/pavan10994/mlops-pipeline-california-housing.mlflow)
set MLFLOW_TRACKING_USERNAME=pavan10994
set MLFLOW_TRACKING_PASSWORD=YOUR_DAGSHUB_TOKEN
```

**Linux / macOS / Git Bash:**
```bash
export MLFLOW_TRACKING_URI="[https://dagshub.com/pavan10994/mlops-pipeline-california-housing.mlflow](https://dagshub.com/pavan10994/mlops-pipeline-california-housing.mlflow)"
export MLFLOW_TRACKING_USERNAME="pavan10994"
export MLFLOW_TRACKING_PASSWORD="YOUR_DAGSHUB_TOKEN"
```

### Step 4: Execute Pipeline Stages
Run the modular stages sequentially in your terminal:

```bash
python src/mlProject/pipeline/stage_01_data_ingestion.py
python src/mlProject/pipeline/stage_02_data_validation.py
python src/mlProject/pipeline/stage_03_data_transformation.py
python src/mlProject/pipeline/stage_04_model_trainer.py
python src/mlProject/pipeline/stage_05_model_evaluation.py
```

### Step 5: Launch Web App Locally
```bash
python app.py
```
Open your web browser and go to `http://localhost:8080`.

---

## 🐳 Docker Containerization & Deployment

### Step 1: Build Docker Image
```bash
docker build -t mlops-california-housing .
```

### Step 2: Run Docker Container
```bash
docker run -p 8080:8080 mlops-california-housing
```
Access the running application inside the Docker container at `http://localhost:8080`.
