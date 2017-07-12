import json
import os

import firebase_admin
import logging

import RPi.GPIO as GPIO
from google.oauth2 import service_account
from firebase_admin.credentials import _scopes, Base

from button.constants import FIREBASE_CREDENTIAL_KEY, GPIO_PIN, FB_UID, FB_DB_URL
from button.handlers import main_loop


# Set up logging
logging.basicConfig(
    format='[%(asctime)s] [%(name)s / %(threadName)s / %(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger('Root')


class ENVCredntial(Base):

    _CREDENTIAL_TYPE = 'service_account'

    def __init__(self):
        env = os.getenv(FIREBASE_CREDENTIAL_KEY)
        if env is None:
            raise RuntimeError(FIREBASE_CREDENTIAL_KEY + 'environment valirable is not set.'
                               'See README.md for details on obtaining the key.')
        json_data = json.loads(env)
        logger.debug('Firebase credential is valid JSON')
        if json_data.get('type') != self._CREDENTIAL_TYPE:
            raise ValueError('Invalid certificate file. File must contain a '
                             '"type" field set to "{0}".'.format(self._CREDENTIAL_TYPE))
        self._project_id = json_data.get('project_id')
        try:
            self._g_credential = service_account.Credentials.from_service_account_info(
                json_data, scopes=_scopes)
        except ValueError as error:
            raise ValueError('Failed to initialize a certificate credential. '
                             'Caused by: "{0}"'.format(error))


def main():
    logger.info('Initializing')

    firebase_admin.initialize_app(ENVCredntial(), {
        'databaseURL': FB_DB_URL,
        'databaseAuthVariableOverride': {
            'uid': FB_UID
        }
    })
    logger.debug('Firebase initialized')

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    logger.debug('GPIO setup completed')

    logger.info('Initialization completed. Entering loop')
    main_loop()

if __name__ == '__main__':
    try:
        main()
    except:
        GPIO.cleanup()
        raise

