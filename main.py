from typing import Any

from fastapi import FastAPI

from core.data_models import Data, Predictions
from core.prediction import get_model, make_predictions

app = FastAPI()

model = get_model()


@app.post("/prediction", response_model=Predictions)
async def prediction(data: Data) -> Any:
    """
    Handles prediction requests by processing input data and returning predictions.

    Parameters
    ----------
        data : Data
            The input data containing a dictionary of features for multiple records.

    Returns
    -------
        Predictions
            A dictionary mapping record IDs to their predicted class labels.
    """
    result = make_predictions(data, model)
    return Predictions(predictions=result)
