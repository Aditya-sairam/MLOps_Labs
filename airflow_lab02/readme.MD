# Wine Data Flow Pipeline

The following lab repo contains the Airflow data pipeline orchestration for the Wine dataset available in the scikit-learn package.

## File Structure

```bash
05-airflow-lab/
├── dags/
│   ├── airflow.py
│   └── src/
│       └── wine_pipeline.py
├── logs/
├── plugins/
├── config/
├── docker-compose.yaml
├── requirements.txt
├── .env
└── README.md
```

## Description

- **dags/src/**: Contains the Python script necessary for loading data, cleaning, and training the model
- **dags/airflow.py**: Contains the Airflow orchestration required to orchestrate between tasks
- **docker-compose.yaml**: Contains the Docker Compose code to build and run the Airflow image in a Docker container

## How to Run the Workflow

1. Clone the repo

2. Set up environment variables:
   ```bash
   echo "AIRFLOW_UID=$(id -u)" > .env
   echo "_PIP_ADDITIONAL_REQUIREMENTS=scikit-learn pandas numpy" >> .env
   ```

3. Initialize Airflow:
   ```bash
   docker-compose up airflow-init
   ```

4. Start Airflow:
   ```bash
   docker-compose up -d
   ```

5. Navigate to `http://localhost:8080`

6. Login using:
   - **Username**: `airflow`
   - **Password**: `airflow`

7. Navigate to the DAG `wine_ml_pipeline`

8. Run the DAG

## Pipeline Tasks

```
load_data → clean_data → train_model → evaluate_model
```