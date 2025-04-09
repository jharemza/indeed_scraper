#!/bin/bash

source "C:\Users\ubiqu\anaconda3\etc\profile.d\conda.sh"
conda activate indeed_scraper

ENV_NAME="indeed_scraper"
DATE_TAG=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_DIR="env_logs"
LOG_FILE="${LOG_DIR}/environment_${DATE_TAG}.yml"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

echo "[INFO] Exporting conda environment: $ENV_NAME"
conda activate $ENV_NAME

# Export full and historical environment snapshots
conda env export --from-history > environment.yml
conda env export > "$LOG_FILE"

echo "[INFO] Updated environment.yml"
echo "[INFO] Snapshot saved to $LOG_FILE"
