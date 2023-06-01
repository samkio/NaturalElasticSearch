from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import boto3
import os

host = os.environ['OS_CLUSTER_ENDPOINT']
region = 'us-west-2'
service = 'es'
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, service)

client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection,
    pool_maxsize = 20
)

def handler(event, context):
    print("Hello world!")