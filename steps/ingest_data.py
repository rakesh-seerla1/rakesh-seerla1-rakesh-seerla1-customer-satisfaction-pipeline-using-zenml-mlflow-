from zenml import step
import pandas as pd
from src.data_config import DataConfig  # Correct import
  # Import DataConfig

@step
def ingest_df(config: DataConfig) -> pd.DataFrame:
    """Reads data from CSV using the provided config."""
    print(f"Reading data from: {config.data_path}")
    
    df = pd.read_csv(config.data_path)
    print(f"Data loaded successfully. Shape: {df.shape}")
    return df
