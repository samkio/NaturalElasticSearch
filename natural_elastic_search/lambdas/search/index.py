from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import boto3
import os

host = os.environ["OS_CLUSTER_ENDPOINT"]
region = boto3.session.Session().region_name
service = "es"
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, service)

client = OpenSearch(
    hosts=[{"host": host, "port": 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
    pool_maxsize=20,
)


def handler(event, context):
    index_name = "docs"

    client.index(
        index=index_name,
        body={"title": "Moneyball", "director": "Bennett Miller", "year": "2011"},
        id="1",
        refresh=True,
    )
    client.index(
        index=index_name,
        body={
            "title": "Star Wars: Episode I - The Phantom Menace",
            "director": "George Lucas",
            "year": "1999",
        },
        id="2",
        refresh=True,
    )
    client.index(
        index=index_name,
        body={"title": "28 Days Later", "director": "Danny Boyle", "year": "2002"},
        id="3",
        refresh=True,
    )
    client.index(
        index=index_name,
        body={"title": "Shaun of the Dead", "director": "Edgar Wright", "year": "2004"},
        id="4",
        refresh=True,
    )
    client.index(
        index=index_name,
        body={
            "title": "The Grand Budapest Hotel",
            "director": "Wes Anderson",
            "year": "2014",
        },
        id="5",
        refresh=True,
    )

    q = "miller"
    query = {
        "size": 5,
        "query": {"multi_match": {"query": q, "fields": ["title^2", "director"]}},
    }

    response = client.search(body=query, index=index_name)
    print("\nSearch results:")
    print(response)
