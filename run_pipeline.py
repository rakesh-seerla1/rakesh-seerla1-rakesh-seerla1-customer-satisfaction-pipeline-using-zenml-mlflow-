import os
from pipelines.training_pipeline import train_pipeline
from src.data_config import DataConfig
from zenml.client import Client

if __name__ == "__main__":
    # Create config object
    config = DataConfig()

    # Print active stack's experiment tracker URI
    print(Client().active_stack.experiment_tracker.get_tracking_uri())

    # Example of a simple log
    logs_dir = 'C:\\Users\\seerl\\OneDrive\\Desktop\\project-1\\local_store\\ingest_df'
    os.makedirs(logs_dir, exist_ok=True)
    logs_path = os.path.join(logs_dir, 'logs.txt')
    with open(logs_path, 'w') as file:
        file.write('Log content')
    
    # Pass config to the pipeline
    train_pipeline(config)

