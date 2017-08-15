# rpi-button
Detect mail existence in RPi and respond in firebase

Because of laziness, the package name show button. But it in fact requires
distance sensor to complete the task.

__WARNING__: This script is designed to run on _ARM_ architecture. x64 computer will not able to run this script.

## Set up GPIO port
Set up distance sensor according to [this tutorial](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi). Follow GPIO pins in that tutorial.

## Set up service account
Follow [instruction from Firebase](https://firebase.google.com/docs/admin/setup) and get the service account information.

Then, save the file to `~/firebase-adminsdk.json`.

## Install dependencies
Run the following commands:
```bash
sudo apt-get update # Update package database
sudo apt-get install python3 python3-pip # Install python compiler/interpreter
sudo pip3 install setuptools # Install python dependency
sudo pip3 install pipenv # Install pipenv, package management for python
pipenv --three install --dev # Install local dependencies
```

## Execution
__Remember to set Firebase service key first__
```bash
pipenv run python main.py
```
