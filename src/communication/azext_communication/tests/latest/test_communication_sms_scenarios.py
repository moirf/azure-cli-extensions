from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer, CommunicationResourcePreparer
from .utils import get_new_phonenumber, get_test_recipient_phonenumber, get_test_source_phonenumber
import os

class CommunicationSmsScenarios(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_send_sms(self, communication_resource_info):

        if self.is_live:
            os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        sender = get_test_source_phonenumber(self.is_live)
        recipient = get_test_recipient_phonenumber(self.is_live)

        if sender is None:
            sender = get_new_phonenumber(communication_resource_info[1])

        if recipient is None:
            recipient = sender;

        self.kwargs.update({
            'sender' : sender,
            'recipient': recipient})

        self.cmd('az communication sms send-sms --sender \"{sender}\" \
        --recipient \"{recipient}\" --message "Hello there!!"', checks=[
            self.check("[0].errorMessage", None),
            self.check("[0].httpStatusCode", "202"),
            self.check("[0].successful", "True")
        ])