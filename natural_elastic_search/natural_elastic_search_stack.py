from aws_cdk import Stack, RemovalPolicy
from aws_cdk.aws_opensearchservice import Domain, EngineVersion
from aws_cdk.aws_lambda import Function, Runtime, Code
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

        searchFunction = Function(
            self,
            "SearchFunction",
            code=Code.from_asset(
                path.join(path.dirname(path.abspath(__file__)), "handler")
            ),
            handler="search_lambda.main",
            runtime=Runtime.PYTHON_3_10,
        )
