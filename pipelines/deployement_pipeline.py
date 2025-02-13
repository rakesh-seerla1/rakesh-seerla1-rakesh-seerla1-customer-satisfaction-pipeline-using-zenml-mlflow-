import numpy as np 
import pandas as pd
# from materializer.custom_materializer import cs_materializer
from zenml import pipelines,step
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (MLFlowModelDeployer,
                                                                             )

from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
# from pydantic import BaseModel
# from zenml.steps import Output

from steps.clean_data import  clean_df
from steps.evaluation import evaluate_model
from steps.ingest_data import ingest_df
from steps.model_train import train_model


docker_settings = DockerSettings(required_integrations=[MLFLOW])




from pydantic import BaseModel

class DeploymentTriggerConfig(BaseModel):
    """Deployment trigger config"""
    accuracy_threshold: float = 0.92  # ✅ Renamed from min_accuracy




@step
def deployment_trigger(
    accuracy:float,
    config: DeploymentTriggerConfig = DeploymentTriggerConfig(),

):
    """ implement a simple model deployment trigger that looks at the input model accyracy if it is greater than 0,92 to deploy else dosent deploy"""
    return accuracy > config.min_accuracy


@pipelines.pipeline(enable_cache=True, settings={"docker":docker_settings})
def continous_deployment_pipeline(
    data_path: str,
    min_accuracy: float = 0.92,
    workers: int=1,
    timeout:int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
    df = ingest_df(data_path)
    X_train,X_test,y_train,y_test = clean_df(df)
    model = train_model(X_train,X_test,y_train,y_test)
    r2_score,rmse = evaluate_model(model,X_test,y_test)
    deployment_decision = deployment_trigger(r2_score)
    mlflow_model_deployer_step(
        model=model,
        deploy_decision=deployment_decision,
        workers=workers,
        timeout=timeout,
    )


from zenml import pipelines

@pipelines.pipeline(enable_cache=True)
def inference_pipeline():
    """A simple inference pipeline placeholder"""
    print("Inference pipeline executed!")
