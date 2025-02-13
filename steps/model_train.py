import logging
from zenml import step
from sklearn.base import RegressorMixin
import pandas as pd
import mlflow
from zenml.client import Client



from src.model_dev import LinearRegressionModel 

from steps.config import ModelNameConfig

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
    config: ModelNameConfig,
) -> RegressorMixin:
    """
    Placeholder step for model training.

    Args:
        df (pd.DataFrame): ingested_data.

    Returns:
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,.
    """

    try:
        model = None
        if config.model_name == "LinearRegression":
            mlflow.sklearn.autolog()
            model = LinearRegressionModel()
            trained_model = model.train(X_train, y_train)
            return trained_model
        else:
            raise ValueError("model {} not supported".format(config.model_name))
    except Exception as e:
        logging.error(f"Error in training the model {str(e)}")
        raise e

    

