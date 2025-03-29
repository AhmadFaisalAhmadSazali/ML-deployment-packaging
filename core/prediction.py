import os
import pickle

import pandas as pd

from core.data_models import Data


def get_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, "trained_model.pkl")

    with open(model_path, "rb") as file:
        return pickle.load(file)


def make_predictions(data: Data, model) -> dict[int, int]:
    """
    A function to make predictions on passed data using trained model.

    Parameters
    ----------
    data : Data
        A `Data` pydantic base model object.

    Returns
    -------
    A dictionary of key-value pairs where the key is id of predicted sample and value is prediction of the binary classification. Value can be 0 or 1.
    """
    index = data.data.keys()
    processed_data = {idx: values.model_dump() for idx, values in data.data.items()}
    input_data = pd.DataFrame.from_dict(processed_data, orient="index")
    predictions = model.predict(input_data).tolist()
    return {key: value for key, value in zip(index, predictions)}
