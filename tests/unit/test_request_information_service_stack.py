import aws_cdk as core
import aws_cdk.assertions as assertions

from request_information_service.request_information_service_stack import RequestInformationServiceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in request_information_service/request_information_service_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RequestInformationServiceStack(app, "request-information-service")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
