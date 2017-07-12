# rpi-button
Detect button press in RPi and respond in firebase

__WARNING__: This script is designed to run on _ARM_ architecture. x64 computer will not able to run this script.

## Set up GPIO port
Connect the switch to GPIO 18 and Ground. (Chart [here](http://www.mediafire.com/download/dp0sbulael9ns2a/Raspberry_Pi_GPIO_Pintout_diagram_v2.pdf))

## Set up service account
Follow [instruction from Firebase](https://firebase.google.com/docs/admin/setup) and get the service account information.

Then, save the file to `~/firebase-adminsdk.json`.

## Install dependencies
Run the following commands:
```bash
sudo apt-get update # Update package database
sudo apt-get install python3 python3-pip # Install python interpolator
sudo pip3 install setuptools # Install python dependency
sudo pip3 install pipenv # Install pipenv, package management for python
pipenv --three install --dev # Install local dependencies
```

## Execution
__Remember to set Firebase service key first__
```bash
pipenv run python main.py
```
