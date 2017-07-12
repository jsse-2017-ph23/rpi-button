import threading
from time import sleep

import RPi.GPIO as GPIO
import logging

from firebase_admin import db

from .constants import GPIO_PIN, MAIL_COUNT_PATH

button_num = 0
button_num_lock = threading.Lock()
logger = logging.getLogger('Handlers')


class Update(threading.Thread):
    def run(self):
        # Because Firebase python do not have transaction
        global button_num

        ref = db.reference(MAIL_COUNT_PATH)
        value = ref.get()
        logger.debug('Got old value. Value: %s', value)
        with button_num_lock:
            new_value = value + button_num
            button_num = 0
        logger.debug('Setting value to %s', new_value)
        ref.set(new_value)
        logger.debug('Set completed')


def main_loop():
    global button_num
    button_pressed = not GPIO.input(GPIO_PIN)
    logger.debug('Initial input state: %s', button_pressed)
    while True:
        sleep(0.2)
        new_button_pressed = not GPIO.input(GPIO_PIN)

        if button_pressed and not new_button_pressed:
            logger.debug('Press released.')
            with button_num_lock:
                button_num += 1
            if button_num == 1:  # Thread not started. Start update process.
                logger.debug('Update thread not started. Starting the thread')
                thread = Update()
                thread.start()

        button_pressed = new_button_pressed
