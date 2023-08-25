#!/bin/bash

# Activate your virtual environment if needed
# source /path/to/your/venv/bin/activate

# Navigate to the directory containing this script
cd "$(dirname "$0")"

# Set environment variables if needed
# export DATABASE_URL="your_database_url"
# export API_KEY="your_api_key"

# Run data extraction script
python code/data_extraction/extract_data.py

# Run model training script
python code/model_training/train_model.py

# Run forecast deployment script
python code/forecast_deployment/deploy_forecasts.py

# Deactivate virtual environment if needed
# deactivate

echo "Pipeline execution completed."
