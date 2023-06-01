import aws_cdk as core
import aws_cdk.assertions as assertions

from natural_elastic_search.natural_elastic_search_stack import NaturalElasticSearchStack

# example tests. To run these tests, uncomment this file along with the example
# resource in natural_elastic_search/natural_elastic_search_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NaturalElasticSearchStack(app, "natural-elastic-search")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
