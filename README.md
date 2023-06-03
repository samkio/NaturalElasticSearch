# opensearch-natural-language-python-cdk-example

Query OpenSearch indices with natural language.

This is an example application that showcases LLMs ability
to translate natural language into OpenSearch/ElasticSearch
queries that can be used to return results to the user.

The application is written in Python and utilizes AWS via CDK IaC. 

![](docs/diagram.drawio.svg)

1. The user asks a question in natural language.
   - This is hardcoded in the lambda in this example.
2. The lambda calls OpenAI text-davinci model to convert query into an OpenSearch query.
   - OpenAI API key managed in secrets manager rather than environment variables for security.
3. OpenSearch queried using response from text-davinci.
4. User receives OpenSearch documents based on their query.

## Examples

OpenSearch movie data:
| title | director | year |
| ----------------------------------------- | -------------- | ---- |
| Moneyball | Bennett Miller | 2011 |
| Star Wars: Episode I - The Phantom Menace | George Lucas | 1999 |
| 28 Days Later | Danny Boyle | 2002 |
| Shaun of the Dead | Edgar Wright | 2004 |
| The Grand Budapest Hotel | Wes Anderson | 2014 |

**Q**: Find all movies that were made after 2010

**A**: Moneyball, 28 Days later, Shaun of the Dead, The Grand Budapest Hotel

**Q**: Find all movies that were directed by George Lucas with Star Wars in the title

**A**: Star Wars: Episode I - The Phantom Menace

## Caveats / Further Improvements

* Provide more data in prompt - The model has to assume the structure of the documents fields. If it understood the schema then it could be made more generic and extensible.
* Validating input and output - both for the user and the model's output. We wish to avoid giving OpenSearch bad queries and similarly sending user prompts to the language model raw could lead to hijacking.
* Model fine tuning - having a specific language model for open search queries could yield better results. 
* Testing, DevOps etc

## Development

This project is setup for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation
- `python -m pytest` runs unit tests

## Notes

Docker must be installed to bundle the python lambda with the appropriate packages.
