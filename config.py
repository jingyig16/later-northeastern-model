import os

# Base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for images, normalized data, models, and logs
FOLDER_PATH = os.path.join(BASE_DIR, "images")
OUTPUT_PATH = os.path.join(BASE_DIR, "normalized_data")
MODEL_PATH = os.path.join(BASE_DIR, "models")
LOGS_PATH = os.path.join(BASE_DIR, "logs")
