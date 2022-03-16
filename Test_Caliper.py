import pigpio as GPIO
import time
import sys
from datetime import datetime

pi = GPIO.pi()

Caliper_DataPin = 16
Caliper_ClkPin = 18

pi.set_mode(Caliper_DataPin, GPIO.INPUT)
pi.set_mode(Caliper_ClkPin, GPIO.INPUT)

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

while True:
    print("Start loop")
    time.sleep(2)
    print("Sleep 2 seconds")
    print(CaliperData())
    print("Done getting caliper data")