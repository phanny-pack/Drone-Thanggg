#!/usr/bin/python
import spidev
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Shown as pin
#GPIO.setup(16, GPIO.IN)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

resistanceSPIByte = 0x1FF

while True:
    
#    voltageValue = GPIO.input(16)
    voltageValue = input("Enter high or low voltage: ")
    if voltageValue == 'high':
        print('Voltage is high.')
        resistanceSPIByte -= 1
        
    print('Writing ' + str(resistanceSPIByte) + ' to digital pot...')
    write_pot(resistanceSPIByte)   
      