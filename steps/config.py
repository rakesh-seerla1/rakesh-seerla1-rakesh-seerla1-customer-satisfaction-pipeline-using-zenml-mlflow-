from pydantic import BaseModel  # ✅ Use Pydantic's BaseModel instead!

class ModelNameConfig(BaseModel):  # ✅ BaseModel replaces BaseConfig
    """
    Model configs
    """
    model_name: str = "LinearRegression"
