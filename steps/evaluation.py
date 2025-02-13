import logging
import mlflow
from typing import Tuple
from zenml import step
import pandas as pd
from sklearn.base import RegressorMixin
from typing_extensions import Annotated
from zenml.client import Client
from pydantic import BaseModel

# Import evaluation strategies
from src.evaluation import MSE, R2, RMSE  

# ✅ Fix: Properly configure Pydantic model
class DeploymentConfig(BaseModel):
    model_name: str = "default_model"

    class Config:
        protected_namespaces = ()  # ✅ Fix for Pydantic namespace warning

# ✅ Ensure experiment tracker is properly retrieved
experiment_tracker = Client().active_stack.experiment_tracker
if experiment_tracker is None:
    raise ValueError("No active experiment tracker found in the ZenML stack.")

# Import evaluation strategies
from src.evaluation import MSE, R2, RMSE  

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def evaluate_model(
    model: RegressorMixin, 
    X_test: pd.DataFrame,
    y_test: pd.DataFrame,
) -> Tuple[float, float, float]:  # ✅ Correct return type (Tuple)
    """
    Evaluate the model using the test data.

    Args:
        model: The trained model.
        X_test: The test features.
        y_test: The test target variable.

    Returns:
        Tuple containing R2 Score, MSE, and RMSE.
    """
    try:
        # Make predictions
        prediction = model.predict(X_test)

        # Calculate evaluation metrics using the correct method (`evaluate()`)
        mse_class = MSE()
        mse = mse_class.evaluate(y_test, prediction)  # ✅ Fixed
        mlflow.log_metric("MSE", mse)  # ✅ Fixed

        r2_class = R2()
        r2_score = r2_class.evaluate(y_test, prediction)  # ✅ Fixed
        mlflow.log_metric("R2", r2_score)  # ✅ Fixed

        rmse_class = RMSE()
        rmse = rmse_class.evaluate(y_test, prediction)  # ✅ Fixed
        mlflow.log_metric("RMSE", rmse)  # ✅ Fixed

        return r2_score, mse, rmse  # ✅ Now returns a tuple, matching function signature
    except Exception as e:
        logging.error(f"Error in evaluating the model: {str(e)}")
        raise e
