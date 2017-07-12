const {Gpio} = require('onoff')
const admin = require('firebase-admin')

const FB_UID = 'worker-rpi'
const MAIL_COUNT_PATH = '/mailCount'
const GPIO_PIN = 18
const SERVICE_ACCOUNT = JSON.parse(process.env.FIREBASE_SERVICE_KEY)

console.log('Initializing Firebase admin')
// Initialization
admin.initializeApp({
  credential: admin.credential.cert(SERVICE_ACCOUNT),
  databaseURL: 'https://jsse-2017.firebaseio.com',
  databaseAuthVariableOverride: {
    uid: FB_UID
  }
})

console.log('Initializing button GPIO')
const button = new Gpio(GPIO_PIN, 'in', 'both')

// Set up clean up first
process.on('SIGINT', () => {
  button.unexport()
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
