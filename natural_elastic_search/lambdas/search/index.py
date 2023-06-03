from adapter.open_search import OpenSearchClient
from adapter.secrets_manager import SecretsManagerSecret
from adapter.open_ai import OpenAIClient
import os

os_client = OpenSearchClient(os.environ["OS_CLUSTER_ENDPOINT"], "docs")
openai_api_key = SecretsManagerSecret(os.environ["OPEN_AI_API_KEY_SECRET"]).get_value()
openai_client = OpenAIClient(openai_api_key)


def handler(event, context):
    # Pre-load data into the OS cluster
    os_client.index(
        [
            {"title": "Moneyball", "director": "Bennett Miller", "year": "2011"},
            {
                "title": "Star Wars: Episode I - The Phantom Menace",
                "director": "George Lucas",
                "year": "1999",
            },
            {"title": "28 Days Later", "director": "Danny Boyle", "year": "2002"},
            {"title": "Shaun of the Dead", "director": "Edgar Wright", "year": "2004"},
            {
                "title": "The Grand Budapest Hotel",
                "director": "Wes Anderson",
                "year": "2014",
            },
        ]
    )

    # Perform search
    response = os_client.search(
        {
            "size": 5,
            "query": {
                "multi_match": {"query": "miller", "fields": ["title^2", "director"]}
            },
        }
    )
    print("\nSearch results:")
    print(response)
