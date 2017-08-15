import time
import logging

from RPi import GPIO

from button.constants import DIST_TRIG_PIN, DIST_ECHO_PIN, DIST_THRESHOLD, UPDATE_INTERVAL
from button.dbupdate import DBUpdate

logger = logging.getLogger('rpi-button distance sensor')


def measure_distance() -> float:
    logger.debug('Measuring distance')
    # Trigger
    GPIO.output(DIST_TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(DIST_TRIG_PIN, False)

    while GPIO.input(DIST_ECHO_PIN) == 0:
        # Set the variable to the time when echo pin is 1
        pulse_start = time.time()

    while GPIO.input(DIST_ECHO_PIN) == 1:
        # Set the variable to the time when echo is 0
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)


def have_mail() -> bool:
    s = measure_distance()
    return s <= DIST_THRESHOLD


def loop_distance_sensor():
    logger.debug('Setting up distance sensor GPIO ports')
    GPIO.setup(DIST_TRIG_PIN, GPIO.OUT)
    GPIO.setup(DIST_ECHO_PIN, GPIO.IN)
    logger.info('Distance sensor GPIO ports set')

    # Warm up distance sensor
    GPIO.output(DIST_TRIG_PIN, False)
    logger.debug('Warming up distance sensor')
    time.sleep(2)
    logger.info('Distance sensor warm up complete')

    # Initial update
    mail = have_mail()
    update_thread = DBUpdate()
    update_thread.add_task(mail)

    while True:
        time.sleep(UPDATE_INTERVAL)
        new_mail = have_mail()

        if mail != new_mail:
            logger.info('Mail status changed. From %s to %s', mail, new_mail)
            update_thread.add_task(mail)

        mail = new_mail
