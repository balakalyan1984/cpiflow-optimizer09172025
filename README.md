# cpiflow-optimizer


## Build & push


# Training image
docker build -t docker.io/<your-namespace>/cpiflow-train:py312-v1 ./train
docker push docker.io/<your-namespace>/cpiflow-train:py312-v1


# Serving image
docker build -t docker.io/<your-namespace>/cpiflow-serve:py312-v1 ./serve
docker push docker.io/<your-namespace>/cpiflow-serve:py312-v1


## AI Core — Training Execution (example bindings)


Inputs:
- parameters:
- TARGET_COLUMN = CUSTOM_STATUS
- DATA_FILE = cpi_logs_500.csv
- artifacts:
- cpiflowdataset → referenceName: default, path: aicoretutorial/cpiflow/trainingdata/cpi_logs_500.csv


Outputs:
- cpiflowmodel → aicoretutorial/cpiflow/models/model.pkl
- cpiflowmetrics → aicoretutorial/cpiflow/models/metrics.json
- cpiflowinsights → aicoretutorial/cpiflow/insights/artifact_insights.csv
- cpiflowhotspots → aicoretutorial/cpiflow/insights/hotspots.csv
- cpiflowreport → aicoretutorial/cpiflow/insights/report.md


## AI Core — Serving Deployment
Create from `cpiflow-serving-pipeline` and bind input artifact:
- cpiflowmodel → aicoretutorial/cpiflow/models/model.pkl (or the specific run’s artifact)


## Test (Postman)
- Import `tests/cpiflow.postman_collection.json`
- Set `baseUrl` to your serving URL and `token` to your OAuth token
- Run: Greet → Analyze → Analyze Many → Analyze All → Predict


## Local smoke tests


# Train locally with mounted CSV (optional)
docker run --rm \
-v "$PWD/cpi_logs_500.csv:/app/data/cpi_logs_500.csv" \
-e DATA_PATH=/app/data/cpi_logs_500.csv \
-e MODEL_DIR=/app/model -e MODEL_PATH=/app/model/model.pkl \
docker.io/<your-namespace>/cpiflow-train:py312-v1


# Serve locally (mount model)
docker run --rm -p 9001:9001 \
-v "$PWD/model.pkl:/mnt/models/model.pkl" \
docker.io/<your-namespace>/cpiflow-serve:py312-v1


# Try cURL
export BASE=http://localhost:9001
bash tests/curl-examples.sh