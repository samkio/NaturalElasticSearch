from aws_cdk import Stack, RemovalPolicy
from aws_cdk.aws_opensearchservice import Domain, EngineVersion
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk.aws_secretsmanager import Secret
from constructs import Construct
from os import path


class NaturalElasticSearchStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        opensearch = Domain(
            self,
            "OpenSearchDomain",
            version=EngineVersion.OPENSEARCH_1_0,
            removal_policy=RemovalPolicy.DESTROY,
        )

        open_api_key_secret = Secret(self, "OpenAPIKeySecret")

        searchFunction = PythonFunction(
            self,
            "SearchFunction",
            entry=path.join(path.dirname(path.abspath(__file__)), "lambdas/search"),
            runtime=Runtime.PYTHON_3_10,
            environment={
                "OS_CLUSTER_ENDPOINT": opensearch.domain_endpoint,
                "OPEN_AI_API_KEY_SECRET": open_api_key_secret.secret_name,
            },
        )
        opensearch.grant_index_read_write("docs", searchFunction)
        open_api_key_secret.grant_read(searchFunction)
