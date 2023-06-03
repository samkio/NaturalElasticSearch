from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
from aws_lambda_powertools import Logger
import boto3
import json

logger = Logger(service="natural_elastic_search.opensearch")


class OpenSearchClient:
    """Encapsulates OpenSearch functions."""

    def __init__(self, host: str, index_name: str):
        """
        :param host: A OpenSearch host to connect to.
        :param index_name: An OpenSearch index to use.
        """
        region = boto3.session.Session().region_name
        service = "es"
        credentials = boto3.Session().get_credentials()
        auth = AWSV4SignerAuth(credentials, region, service)
        self.open_search_client = OpenSearch(
            hosts=[{"host": host, "port": 443}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            pool_maxsize=20,
        )
        self.index_name = index_name

    def index_docs(self, docs: list):
        """
        Indexes documents into the OpenSearch service

        :param docs: The documents to index.
        """

        try:
            for id, doc in enumerate(docs):
                self.open_search_client.index(
                    index=self.index_name,
                    body=doc,
                    id=id,
                    refresh=True,
                )
        except Exception as e:
            logger.exception("Couldn't index documents %s.", self.index_name)
            logger.exception(e)
            raise

    def query(self, query: str):
        """
        Queries documents from the OpenSearch service

        :param query: The query to use.
        :return: The response from the query.
        """

        try:
            body = json.loads(query)
            response = self.open_search_client.search(body=body, index=self.index_name)
        except Exception as e:
            logger.exception("Couldn't query index %s.", self.index_name)
            logger.exception(e)
            raise
        else:
            return response
