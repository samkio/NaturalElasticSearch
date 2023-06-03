import openai


class OpenAIClient:
    """Encapsulates OpenAI functions."""

    def __init__(self, api_key: str):
        """
        :param api_key: An OpenAI key to use.
        """
        self.api_key = api_key

    def query_to_open_search_query(self, query: str) -> str:
        openai.api_key = self.api_key
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
        return response.choices[0].text.strip().removesuffix(",")
