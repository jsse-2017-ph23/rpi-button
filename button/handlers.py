import threading
from time import sleep
import logging

import RPi.GPIO as GPIO
from firebase_admin import db

from .constants import BUTTON_GPIO_PIN, HAVE_MAIL_PATH, UPDATE_INTERVAL

logger = logging.getLogger('Handlers')


def update(have_mail: bool):
    ref = db.reference(HAVE_MAIL_PATH)
    logger.debug('Setting have mail to value: %s', have_mail)
    ref.set(have_mail)
    logger.debug('Setting have mail succeed. Current value: %s', have_mail)


def main_loop():
    button_pressed = not GPIO.input(BUTTON_GPIO_PIN)
    logger.debug('Initial input state: %s', button_pressed)
    threading.Thread(target=update, args=(button_pressed,))  # Initial update

    while True:
        sleep(UPDATE_INTERVAL)
        new_button_pressed = not GPIO.input(BUTTON_GPIO_PIN)

        if button_pressed and not new_button_pressed:
            logger.debug('Button status changed. From %s to %s', button_pressed, new_button_pressed)
            threading.Thread(target=update, args=(new_button_pressed,))

        button_pressed = new_button_pressed
