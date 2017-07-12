const {Gpio} = require('onoff')
const admin = require('firebase-admin')

const FB_UID = 'worker-rpi'
const MAIL_COUNT_PATH = '/mailCount'
const GPIO_PIN = 18
const FIREBASE_CREDENTIAL_KEY = 'FIREBASE_SERVICE_KEY'

console.log('Initializing Firebase admin')
const firebaseKeyRaw = process.env[FIREBASE_CREDENTIAL_KEY]
try {
  const parsedFirebaseKey = JSON.parse(firebaseKeyRaw)
  admin.initializeApp({
    credential: admin.credential.cert(parsedFirebaseKey),
    databaseURL: 'https://jsse-2017.firebaseio.com',
    databaseAuthVariableOverride: {
      uid: FB_UID
    }
  })
} catch (err) {
  if (err instanceof SyntaxError) {
    console.error(`Invalid JSON file in ${FIREBASE_CREDENTIAL_KEY}. Or you have not set it?`)
  }
  throw err
}

console.log('Initializing button GPIO')
const button = new Gpio(GPIO_PIN, 'in', 'both')

// Set up clean up first
process.on('SIGINT', () => {
  button.unexport()
  console.log('Cleanup completed')
})

console.log('Initialization completed')

// KeyUp handler, like in browser
function onKeyUp() {
  const database = admin.database()
  return database.ref(MAIL_COUNT_PATH).transaction(value => value + 1)
}

console.log('Reading the button for the first time.')
let buttonPressed = !!button.readSync()
console.log('Button pressed?', buttonPressed)

button.watch((err, value) => {
  if (err) {
    throw err
  }
  const newPressed = !!value
  console.log('Button pressed changed. New value:', value)
  if (buttonPressed && !newPressed) {
    console.log('Button press is released. Firing callback.')
    onKeyUp()
  }
  buttonPressed = newPressed
})
