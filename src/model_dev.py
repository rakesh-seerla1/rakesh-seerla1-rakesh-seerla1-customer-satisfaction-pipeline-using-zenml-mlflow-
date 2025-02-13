import logging
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression


class Model(ABC):
    """
    Abstract class for model development

    """
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Abstract class for model development
        Args:
        x_train: training data
        y_train: training target
        returns:
        none
        """
        pass
#taking simple linear regression
class LinearRegressionModel(Model):
    """
    Class for linear regression model development

    """
    def train(self,X_train,y_train,**kwargs):
        """
        train the model 

        Args:
            x_train : training data
            y_train): training target
        Returns:
            none
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model trained successfully")
            return reg
        except Exception as e:
            logging.error(f"Error in training the model {str(e)}")
            raise e
        
            
    