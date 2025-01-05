from typing import Any

from fastapi import FastAPI

from core.data_models import Data, Predictions
from core.prediction import make_predictions

app = FastAPI()


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
    result = make_predictions(data)
    return Predictions(predictions=result)
