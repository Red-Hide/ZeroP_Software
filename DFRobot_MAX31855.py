# -*- coding: utf-8 -*-
import time
import sys
import pigpio as GPIO

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
  
