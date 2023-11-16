from os import environ
import sys
from pyicloud import PyiCloudService


def login(email: str, password: str) -> PyiCloudService:
    api = PyiCloudService(email, password)

    if api.requires_2fa:
        code = input("Enter the code you received of one of your approved devices: ")
        result = api.validate_2fa_code(code)

        if not result:
            raise Exception("failed to verify security code")
        
        if not api.is_trusted_session:
            result = api.trust_session()
            if not result:
                raise Exception("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
    # elif api.requires_2sa:
    #     import click
    #     print("Two-step authentication required. Your trusted devices are:")

    #     devices = api.trusted_devices
    #     for i, device in enumerate(devices):
    #         print(
    #             "  %s: %s" % (i, device.get('deviceName',
    #             "SMS to %s" % device.get('phoneNumber')))
    #         )

    #     device = click.prompt('Which device would you like to use?', default=0)
    #     device = devices[device]
    #     if not api.send_verification_code(device):
    #         print("Failed to send verification code")
    #         sys.exit(1)

    #     code = click.prompt('Please enter validation code')
    #     if not api.validate_verification_code(device, code):
    #         print("Failed to verify verification code")
    #         sys.exit(1)
    return api

