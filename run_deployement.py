from pipelines.deployement_pipeline import continous_deployment_pipeline,inference_pipeline
import click
from src.data_config import DataConfig




from rich import print
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)


DEPLOY ="deploy"
PREDICT = "predict"
DEPLOY_AND_PREDICT = "deploy_and_predict"






@click.command()
@click.option(
    "--config",
    "-c",
    type=click.Choice(["DEPLOY", "PREDICT", "DEPLOY_AND_PREDICT"]),
    default="DEPLOY_AND_PREDICT",
    help="Optionally you can choose to only run the deployment "
         "pipeline to train and deploy a model ('deploy') or to "
         "only run a prediction against the deployed model "
         "('predict'). By default, both will be run "
         "('deploy_and_predict')."
)
@click.option(
    "--min-accuracy",
    default=0.92,
    help="Minimum accuracy required to deploy the model"
)

def run_deployment(config: str, min_accuracy: float):
    mlflow_model_deployer_component = MLFlowModelDeployer.get_active_model_deployer()
    deploy = config == DEPLOY or config == DEPLOY_AND_PREDICT
    predict = config == PREDICT or config == DEPLOY_AND_PREDICT
    if deploy :
        data_path = DataConfig()
        continous_deployment_pipeline(min_accuracy=min_accuracy,
                                      workers = 3,
                                      timeout = 60,
                                      )
    
              
    if predict:
        inference_pipeline()
#from zenml repositry
    print(
        "You can run:\n"
        f"[italic green]   mlflow ui --backend-store-uri {get_tracking_uri()}"
        "[/italic green]\n...to inspect your experiment runs within the mlflow"
        " UI.\nYou can find your runs tracked within the "
        "`mlflow_example_pipeline` experiment. There you'll also be able to"
        "compare two or more runs.\n\n"
    )

    #fetch existing services with the same pipeline name ,step name and model name 
    existing_services = mlflow_model_deployer_component.find_model_server(
        pipeline_name="continous_deployment_pipeline",
        step_name="mlflow_model_deployer_step",
        model_name="model"
    )


    if existing_services:
        service = existing_services[0]
        if service.is_running():
            print(
                f"the mlflow prediction server is running locally as a daemon "
                f"process service and accepts inference requests at:\n"
                f"           {service.prediction_url}\n"
                f"to stop the service ,run"
                f"[italic green]`zenml model-deployer models delete"
                f"{str(service.uuid)}`[/italic green]"
            )
        elif service.is_failed():
            print(
                f"The MLflow prediction server failed state:\n"
                f"last state:'{service.status.state.value}'\n"
                f" last error:'{service.status.error_message}'"
            )
    else:
        print(
            "No MLFlow prediction server is currently running. The deployment "
            "pipeline must run first to train a model and deploy it. Execute "
            "the same command with the `--deploy` argument to deploy a model."
        )

if __name__ == "main":
    run_deployment()