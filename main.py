import pickle
from typing import Any

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

with open("model/trained_model.pkl", "rb") as file:
    model = pickle.load(file)

app = FastAPI()


class Features(BaseModel):
    highbp: float
    highchol: float
    cholcheck: float
    bmi: float
    smoker: float
    stroke: float
    heartdiseaseorattack: float
    physactivity: float
    fruits: float
    veggies: float
    hvyalcoholconsump: float
    anyhealthcare: float
    nodocbccost: float
    genhlth: float
    menthlth: float
    physhlth: float
    diffwalk: float
    sex: float
    age: float
    education: float
    income: float


class Data(BaseModel):
    data: dict[int, Features]


class Predictions(BaseModel):
    predictions: dict[int, int]


@app.post("/prediction", response_model=Predictions)
async def make_prediction(features: Data) -> Any:
    index = features.data.keys()
    processed_data = {idx: values.model_dump() for idx, values in features.data.items()}
    input_data = pd.DataFrame.from_dict(processed_data, orient="index")
    predictions = model.predict(input_data).tolist()
    result = {key: value for key, value in zip(index, predictions)}
    return Predictions(predictions=result)
