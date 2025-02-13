from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model
from src.data_config import DataConfig  # ✅ For data-related config
from steps.config import ModelNameConfig  # ✅ For model-related config

@pipeline(enable_cache=True)
def train_pipeline(data_config: DataConfig):  # ✅ Renamed to avoid confusion
    df = ingest_df(data_config)  # Step 1: Ingest data
    X_train, X_test, y_train, y_test = clean_df(df)  # Step 2: Clean data

    model_config = ModelNameConfig()  # ✅ Create the correct model config
    model = train_model(X_train, X_test, y_train, y_test, model_config)  # ✅ Pass correct config

    # Step 4: Evaluate model
    r2_score, mse, rmse = evaluate_model(model, X_test, y_test)  

    return r2_score, mse, rmse  # ✅ Matches updated function return
