import pytest
from pydantic import ValidationError

from core.data_models import Data, Features, Predictions
from core.prediction import get_model, make_predictions


def test_predictions_valid():
    """
    GIVEN a valid predictions dictionary with integer keys and values
    WHEN a Predictions instance is created
    THEN it should be successfully instantiated
    """
    # Given
    predictions = Predictions(predictions={1: 0, 2: 1})
    # When / Then
    assert isinstance(predictions, Predictions)


def test_predictions_invalid():
    """
    GIVEN an invalid predictions dictionary with incorrect key-value types
    WHEN a Predictions instance is created
    THEN it should raise a ValidationError
    """
    # Given / When / Then
    with pytest.raises(ValidationError):
        Predictions(predictions={"invalid_key": "not_an_int"})


def test_get_model():
    """
    GIVEN a trained model file exists
    WHEN get_model is called
    THEN it should return a loaded model instance
    """
    # Given / When
    model = get_model()
    # Then
    assert model is not None


def test_make_predictions():
    """
    GIVEN valid input data and a trained model
    WHEN make_predictions is called
    THEN it should return a dictionary of predictions
    """
    # Given
    model = get_model()
    data = Data(
        data={
            1: Features(
                highbp=1.0,
                highchol=0.0,
                cholcheck=1.0,
                bmi=25.5,
                smoker=0.0,
                stroke=0.0,
                heartdiseaseorattack=1.0,
                physactivity=1.0,
                fruits=1.0,
                veggies=0.0,
                hvyalcoholconsump=0.0,
                anyhealthcare=1.0,
                nodocbccost=0.0,
                genhlth=3.0,
                menthlth=5.0,
                physhlth=2.0,
                diffwalk=0.0,
                sex=1.0,
                age=45.0,
                education=4.0,
                income=6.0,
            )
        }
    )
    # When
    predictions = make_predictions(data, model)
    # Then
    assert isinstance(predictions, dict)
    assert all(
        isinstance(k, int) and isinstance(v, int) for k, v in predictions.items()
    )
