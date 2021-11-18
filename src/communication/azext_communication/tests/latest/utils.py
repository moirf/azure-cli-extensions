# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.communication.phonenumbers import (
    PhoneNumbersClient,
    PhoneNumberCapabilityType,
    PhoneNumberAssignmentType,
    PhoneNumberType,
    PhoneNumberCapabilities
)

TEST_IDENTITY_ID_DEFAULT = "8:acs:ab12b0ea-85ea-4f83-b0b6-84d90209c7c4_0000000d-c2f4-c058-7f07-113a0d00c2e9"
TEST_SOURCE_PHONENUMBER_DEFAULT = "+18334241267"
TEST_RECIPIENT_PHONENUMBER_DEFAULT = "+18334241267" 

def get_from_os_environment(env_name, default):
    import os
    return os.environ[env_name] if env_name in os.environ and os.environ[env_name] != "" else default

def get_test_identity_id(is_live):
    if not is_live:
        return TEST_IDENTITY_ID_DEFAULT
    else:
        return get_from_os_environment("AZURE_COMMUNICATION_IDENTITY_ID", TEST_IDENTITY_ID_DEFAULT)

def get_test_source_phonenumber(is_live):
    if not is_live:
        return TEST_SOURCE_PHONENUMBER_DEFAULT
    else:
        return get_from_os_environment("AZURE_COMMUNICATION_SOURCE_PHONENUMBER", None)

def get_test_recipient_phonenumber(is_live):
    if not is_live:
        return TEST_RECIPIENT_PHONENUMBER_DEFAULT
    else:
        return get_from_os_environment("AZURE_COMMUNICATION_RECIPIENT_PHONENUMBER", None)


def get_new_phonenumber(connection_string):
    try:
        phone_numbers_client = PhoneNumbersClient.from_connection_string(connection_string)
        capabilities = PhoneNumberCapabilities(
            calling = PhoneNumberCapabilityType.INBOUND,
            sms = PhoneNumberCapabilityType.INBOUND_OUTBOUND
        )
        search_poller = phone_numbers_client.begin_search_available_phone_numbers(
            "US",
            PhoneNumberType.TOLL_FREE,
            PhoneNumberAssignmentType.APPLICATION,
            capabilities,
            area_code="833",
            polling = True
        )
        search_result = search_poller.result()
        
        purchase_poller = phone_numbers_client.begin_purchase_phone_numbers(search_result.search_id, polling = True)
        purchase_poller.result()
        if(purchase_poller.status() == 'succeeded'):
            phone_number_list = search_result.phone_numbers
            for phone_number in phone_number_list:
                return phone_number
            
    except Exception as ex:
        return TEST_RECIPIENT_PHONENUMBER_DEFAULT