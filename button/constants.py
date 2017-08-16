import os

# GPIO constants
UPDATE_INTERVAL = 5  # Time between each detect, in seconds
DIST_TRIG_PIN = 23
DIST_ECHO_PIN = 24
DIST_THRESHOLD = 4  # If lower than this distance, mail exist. In cm
DIST_ERR_THRESHOLD = 1000  # If result is larger than this, assume result is error and mail does exist (in cm)

# Firebase constants
FB_UID = 'worker-rpi'
FB_DB_URL = 'https://jsse-2017.firebaseio.com'
HAVE_MAIL_PATH = '/haveMail'
FIREBASE_CREDENTIAL_PATH = os.path.expanduser('~/firebase-adminsdk.json')
