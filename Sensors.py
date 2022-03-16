import pigpio as GPIO
import time
import sys
from datetime import datetime

MAX31855_ADDR = 0x10

pi = GPIO.pi()

class DFRobot_MAX31855:
  def __init__(self):
    self.i2c = pi.i2c_open(1,MAX31855_ADDR)
  
  def readData(self):
    a = pi.i2c_read_byte_data(self.i2c.handle, 0x00)
    b = pi.i2c_read_byte_data(self.i2c.handle, 0x01)
#    c = pi.i2c_read_byte_data(self.i2c.handle, 0x02)
    d = pi.i2c_read_byte_data(self.i2c.handle, 0x03)
    return a,b,d
  
  def readCelsius(self):
    a,b,d = self.readData()
    if(d&0x7):
      return False
    if(a&0x80):
      a = 0xff - a
      b = 0xff - b
      temp = -((((a << 8) | b) >> 2)+1)*0.25
      return temp
    temp = (((a << 8) | b) >> 2)*0.25
    return temp

Caliper_DataPin = 16
Caliper_ClkPin = 18
SafeGuard = 17

pi.set_mode(Caliper_DataPin, GPIO.INPUT)
pi.set_mode(Caliper_ClkPin, GPIO.INPUT)
pi.set_mode(SafeGuard, GPIO.INPUT)

TempSensor = DFRobot_MAX31855()

def GetSensorValues():
    CouvercleState = pi.read(SafeGuard)           # A tester et changer
    Temp = float(TempSensor.readCelsius())
    return { "Sécurisé": CouvercleState, "Température": Temp} # Could use fonctions instead of storing data in variables and could replace with tuples

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

