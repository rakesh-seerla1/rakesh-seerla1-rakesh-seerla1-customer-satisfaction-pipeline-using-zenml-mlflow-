import logging
from zenml import step
import pandas as pd
from src.data_cleaning import DataCleaning, DataDivideStrategy,DatapreProcessStrategy
from typing_extensions import Annotated
from typing import Tuple



@step
def clean_df(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "x_train"],
    Annotated[pd.DataFrame, "x_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"]
]:
    """
    cleans the data and divides it into train and test
    args:
        df: pd.DataFrame : input data
    returns:
            x_train:training_data
            x_test:testing_data
            y_train:training_target
            y_test:testing_target
    Passes data without modification (for now)."""
    
    try:
        process_strategy = DatapreProcessStrategy()
        data_cleaning = DataCleaning(df,process_strategy)
        processed_data = data_cleaning.handle_data()

        #divide strategy
        divide_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data,divide_strategy)
        X_train,X_test,y_train,y_test = data_cleaning.handle_data()
        logging.info("Data cleaning completed")
        return X_train,X_test,y_train,y_test
    except Exception as e:
        logging.error(f"Error in cleaning data: {e}")
        raise e