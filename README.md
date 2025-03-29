# Diabetes Prediction API

This repository provides a FastAPI-based REST API to serve a machine learning model for predicting whether a sample has diabetes. The API allows clients to send health-related feature data and receive predictions, making it suitable for integration with applications requiring health risk analysis. 

## Features
- **Machine Learning Integration**: Utilizes a Scikit-learn model for binary classification of diabetes risk.
- **REST API**: Built with FastAPI for modern, fast, and efficient API services.
- **Scalable Deployment**: Dockerized for easy deployment in any environment.
- **Extensible Design**: Supports multiple records in a single request, making it flexible for batch processing.

---
## Project Structure
```
├── core/
│   ├── data_models.py      # Pydantic models for input validation and response structure
│   ├── prediction.py       # Core logic for loading the model and making predictions
│   └── trained_model.pkl   # Pickled Scikit-learn model, need to be generated and saved here
├── main.py                 # FastAPI entry point for the application
├── data/
│   └── raw/                # Raw dataset for testing and demonstration, need to be downloaded
├── Dockerfile              # Docker configuration for deployment, WIP
├── requirements.txt        # Python dependencies, WIP
└── README.md               # Project documentation
```
## Installation

### Prerequisites
- Python 3.12 or higher
- `pip` and `poetry` for package management
- Docker (optional, for containerized deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmadFaisalAhmadSazali/ML-deployment-packaging.git
   cd machine-learning-serving

2. Install the required dependencies:
   ```bash
   poetry install

3. Run the FastAPI server:
   ```bash
   fastapi dev main.py

### Steps for building and running Docker ML 
1. Build the docker image:
   ```bash
   docker build -t diabetes-prediction .

2. Run the container:
   ```bash
   docker run -d -p 5000:8000 diabetes-prediction

3. Run `endpoint_testing.py` to test the deployed endpoint.