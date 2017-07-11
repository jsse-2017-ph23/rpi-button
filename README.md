# rpi-button
Detect button press in RPi and respond in firebase

__WARNING__: This script is designed to run on _ARM_ architecture. x64 computer will not able to run this script.

## Set up GPIO port
Connect the switch to GPIO 18 and Ground. (Chart [here](http://www.mediafire.com/download/dp0sbulael9ns2a/Raspberry_Pi_GPIO_Pintout_diagram_v2.pdf))

## Set up service account
Follow [instruction from Firebase](https://firebase.google.com/docs/admin/setup) and get the service account information.

Set _CONTENT_ of the JSON file to environment variable `$FIREBASE_SERVICE_KEY`

## Install dependencies
Install Node.JS first. Follow [instruction from official website](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions).

Node 8 and above is recommended. At least Node 6 (Not guaranteed) is required.

After that, run the following scripts
```bash
npm install
```

## Execution
__Remember to set Firebase service key first__
```bash
npm start
```
