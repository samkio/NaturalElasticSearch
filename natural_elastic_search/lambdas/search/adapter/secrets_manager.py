from botocore.exceptions import ClientError
from aws_lambda_powertools import Logger
import boto3

logger = Logger()


class SecretsManagerSecret:
    """Encapsulates Secrets Manager functions."""

    def __init__(self, name):
        """
        :param secretsmanager_client: A Boto3 Secrets Manager client.
        """
        self.secretsmanager_client = boto3.client('secretsmanager')
        self.name = name

    def get_value(self, stage=None):
        """
        Gets the value of a secret.

        :param stage: The stage of the secret to retrieve. If this is None, the
                      current stage is retrieved.
        :return: The value of the secret. When the secret is a string, the value is
                 contained in the `SecretString` field. When the secret is bytes,
                 it is contained in the `SecretBinary` field.
        """
        if self.name is None:
            raise ValueError

        try:
            kwargs = {"SecretId": self.name}
            if stage is not None:
                kwargs["VersionStage"] = stage
            response = self.secretsmanager_client.get_secret_value(**kwargs)
            logger.info("Got value for secret %s.", self.name)
        except ClientError as e:
            logger.exception("Couldn't get value for secret %s.", self.name)
            logger.exception(e)
            raise
        else:
            return response
