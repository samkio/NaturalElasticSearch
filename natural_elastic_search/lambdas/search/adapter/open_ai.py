import openai
from aws_lambda_powertools import Logger

logger = Logger(service="natural_elastic_search.openai")


class OpenAIClient:
    """Encapsulates OpenAI functions."""

    def __init__(self, api_key: str):
        """
        :param api_key: An OpenAI key to use.
        """
        openai.api_key = api_key

    def query_to_open_search_query(self, query: str) -> str:
        """
        Converts natural language query to an open search query

        :param query: The query to translate.
        :return: The open search query as a string.
        """
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="""Convert this text to an OPENSEARCH v1 (ElasticSearch) query 

    Example: Find all movies that were directed by Wes Anderson
    Output: "query": {"multi_match": {"query": "Wes Anderson", "fields": ["title^2", "director"]}},

    """
                + query
                + "\n\nOutput:",
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
        except Exception as e:
            logger.exception("Couldn't call OpenAI")
            logger.exception(e)
            raise
        else:
            return response.choices[0].text.strip().removesuffix(",")
