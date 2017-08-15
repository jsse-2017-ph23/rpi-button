import firebase_admin
import logging

import RPi.GPIO as GPIO
from firebase_admin import credentials

from button.constants import FB_UID, FB_DB_URL, FIREBASE_CREDENTIAL_PATH, DIST_TRIG_PIN, DIST_ECHO_PIN
from button.distance import loop_distance_sensor

# Set up logging
logging.basicConfig(
    format='[%(asctime)s] [%(name)s / %(threadName)s / %(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger('rpi-button')


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

    # Distance sensor setup
    GPIO.setup(DIST_TRIG_PIN, GPIO.OUT)
    GPIO.setup(DIST_ECHO_PIN, GPIO.IN)

    logger.debug('GPIO setup completed')

    logger.info('Initialization completed. Entering loop')
    loop_distance_sensor()

if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()

