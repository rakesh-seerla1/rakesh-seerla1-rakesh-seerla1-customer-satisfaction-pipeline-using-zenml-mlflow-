from pydantic import BaseModel

class DataConfig(BaseModel):
    data_path: str = "C:/Users/seerl/OneDrive/Desktop/project-1/data/olist_customers_dataset.csv"
