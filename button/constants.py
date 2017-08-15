import os

# GPIO constants
UPDATE_INTERVAL = 1
DIST_TRIG_PIN = 23
DIST_ECHO_PIN = 24
DIST_THRESHOLD = 5  # If lower than this distance, mail exist. In cm

# Firebase constants
FB_UID = 'worker-rpi'
FB_DB_URL = 'https://jsse-2017.firebaseio.com'
HAVE_MAIL_PATH = '/haveMail'
FIREBASE_CREDENTIAL_PATH = os.path.expanduser('~/firebase-adminsdk.json')
