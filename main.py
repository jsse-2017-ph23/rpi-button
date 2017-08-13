import firebase_admin
import logging

import RPi.GPIO as GPIO
from firebase_admin import credentials

from button.constants import BUTTON_GPIO_PIN, FB_UID, FB_DB_URL, FIREBASE_CREDENTIAL_PATH
from button.handlers import main_loop


# Set up logging
logging.basicConfig(
    format='[%(asctime)s] [%(name)s / %(threadName)s / %(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger('Root')


def main():
    logger.info('Initializing')

    cred = credentials.Certificate(FIREBASE_CREDENTIAL_PATH)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FB_DB_URL,
        'databaseAuthVariableOverride': {
            'uid': FB_UID
        }
    })
    logger.debug('Firebase initialized')

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    logger.debug('GPIO setup completed')

    logger.info('Initialization completed. Entering loop')
    main_loop()

if __name__ == '__main__':
    try:
        main()
    except:
        GPIO.cleanup()
        raise

