# %%
import pandas as pd
import requests

url = "http://127.0.0.1:8000/prediction"

data = pd.read_csv("data/raw/diabetes_binary_health_indicators_BRFSS2015.csv")
data.columns = data.columns.str.lower()
features = data.drop(columns=["diabetes_binary"])

ten_samples = features.sample(10)
ten_samples_dict = ten_samples.to_dict(orient="index")

payload = {"data": ten_samples_dict}
ten_samples_dict

response = requests.post(url, json=payload)
response

if response.status_code == 200:
    predictions = response.json()
    print("Predictions received from the server:")
    print(predictions)
else:
    print(f"Error: Received status code {response.status_code}")
    print("Details:", response.text)
