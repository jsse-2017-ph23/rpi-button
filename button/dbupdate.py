from threading import Thread
import queue
import logging

from firebase_admin import db

from button.constants import HAVE_MAIL_PATH

logger = logging.getLogger('rpi-button dbupdate')


class DBUpdate(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.queue = queue.LifoQueue()

    def add_task(self, mail: bool):
        self.queue.put(mail)

    def run(self):
        while True:
            mail = self.queue.get()
            update_have_mail(mail)


def update_have_mail(mail: bool) -> None:
    ref = db.reference(HAVE_MAIL_PATH)
    logger.debug('Setting have mail to value: %s', mail)
    ref.set(mail)
    logger.debug('Setting have mail succeed. Current value: %s', mail)