import logging
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from sklearn.metrics import mean_squared_error, r2_score

class Evaluation(ABC):
    """Abstract class for defining strategy for evaluating models."""

    @abstractmethod
    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray):
        """
        Evaluate the model.
        Args:
            y_true: The true values of the target variable.
            y_pred: The predicted values of the target variable.
        Returns:
            The evaluation metric.
        """
        pass

# 1st Strategy: MSE
class MSE(Evaluation):
    """
    Evaluation strategy that uses Mean Squared Error.
    """
    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray):  # ✅ Implemented abstract method
        try:
            logging.info("Calculating Mean Squared Error")
            mse = mean_squared_error(y_true, y_pred)
            logging.info(f"Mean Squared Error: {mse}")
            return mse
        except Exception as e:
            logging.error(f"Error in calculating Mean Squared Error: {str(e)}")
            raise e

# 2nd Strategy: R2 Score
class R2(Evaluation):
    """
    Evaluation strategy that uses R2 Score.
    """
    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray):  # ✅ Implemented abstract method
        try:
            logging.info("Calculating R2 Score")
            r2 = r2_score(y_true, y_pred)
            logging.info(f"R2 Score: {r2}")
            return r2
        except Exception as e:
            logging.error(f"Error in calculating R2 Score: {str(e)}")
            raise e

# 3rd Strategy: RMSE
class RMSE(Evaluation):
    """
    Evaluation strategy that uses Root Mean Squared Error.
    """
    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray):  # ✅ Implemented abstract method
        try:
            logging.info("Calculating Root Mean Squared Error")
            rmse = np.sqrt(mean_squared_error(y_true, y_pred))  # ✅ Fixed RMSE calculation
            logging.info(f"Root Mean Squared Error: {rmse}")
            return rmse
        except Exception as e:
            logging.error(f"Error in calculating Root Mean Squared Error: {str(e)}")
            raise e
