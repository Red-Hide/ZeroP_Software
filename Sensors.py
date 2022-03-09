from base64 import decode
import DFRobot_MAX31855
import pigpio as GPIO
import time
from datetime import datetime

pi = GPIO.pi()

Caliper_DataPin = 16
Caliper_ClkPin = 18

TempSensor = DFRobot_MAX31855.DFRobot_MAX31855()
SafeGuard = 17

pi.set_mode(Caliper_DataPin, GPIO.INPUT)
pi.set_mode(Caliper_ClkPin, GPIO.INPUT)
pi.set_mode(SafeGuard, GPIO.INPUT)

def GetSensorValues():
    CouvercleState = pi.read(SafeGuard)           # A tester et changer
    Temp = float(TempSensor.readCelsius())
    return { "Sécurisé": CouvercleState, "Température": Temp}

def CaliperData():
    while True:
        while pi.read(Caliper_ClkPin):
            pass
        tempmicros = datetime.now().microsecond
        while not pi.read(Caliper_ClkPin):
            pass
        if ((datetime.now().microsecond - tempmicros) > 500):
            return decode()

def decode():
    sign = 1
    value = 0

    for i in range(0,23):
        while pi.read(Caliper_ClkPin):
            pass
        while not pi.read(Caliper_DataPin):
            pass
        if pi.read(Caliper_DataPin):
            if i<20:
                value and 1<<i
            if i==20:
                sign = -1
    result = (value*sign)/100
    return result

