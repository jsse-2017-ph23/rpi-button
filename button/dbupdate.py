import logging

from firebase_admin import db

from button.constants import HAVE_MAIL_PATH

logger = logging.getLogger('rpi-button dbupdate')


def update_have_mail(mail: bool) -> None:
    ref = db.reference(HAVE_MAIL_PATH)
    logger.debug('Setting have mail to value: %s', mail)
    ref.set(mail)
    logger.debug('Setting have mail succeed. Current value: %s', mail)