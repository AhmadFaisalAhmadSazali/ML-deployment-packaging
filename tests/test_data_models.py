import pytest
from pydantic import ValidationError

from core.data_models import (Data, Features,  # Adjust import path if needed
                              Predictions)


def test_features_valid_data():
    """
    GIVEN a valid set of feature values
    WHEN a Features instance is created
    THEN it should be successfully instantiated
    """
    # Given
    features = Features(
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
    # When / Then
    assert isinstance(features, Features)


def test_features_invalid_data():
    """
    GIVEN an invalid data type for a feature
    WHEN a Features instance is created
    THEN it should raise a ValidationError
    """
    # Given / When / Then
    with pytest.raises(ValidationError):
        Features(
            highbp="invalid",
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
        )  # "highbp" should be a float, so this should fail


def test_data_valid():
    """
    GIVEN valid data with integer keys and Features values
    WHEN a Data instance is created
    THEN it should be successfully instantiated
    """
    # Given
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
    # When / Then
    assert isinstance(data, Data)


def test_data_invalid():
    """
    GIVEN an invalid dictionary key type in Data
    WHEN a Data instance is created
    THEN it should raise a ValidationError
    """
    # Given / When / Then
    with pytest.raises(ValidationError):
        Data(
            data={
                "invalid_key": Features(
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
        )  # "invalid_key" should be an int, so this should fail


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
