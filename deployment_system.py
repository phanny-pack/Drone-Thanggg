# from data_logging import IMU_Logging as IMU

import time
import board
import busio
import adafruit_gps
#pip install wiringpi
import wiringpi
import serial

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)

gps = adafruit_gps.GPS(uart, debug=False) # Use UART/pyserial

gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

gps.send_command(b"PMTK220,1000")

ACCELERATION_THRESHOLD = 1 # in m/s^2
GPS_DIFF_THRESHOLD =  0.5 # in m/s
SLEEP_TIME = 1 # in seconds
CHECKS_NEEDED = 5


def deploy():
    print("DEPLOYED!!! XD")
    PIN_NUMBA = 18 # to set   
    # use 'GPIO naming'
    wiringpi.wiringPiSetupGpio()
     
    # set #18 to be a PWM output
    wiringpi.pinMode(PIN_NUMBA, wiringpi.GPIO.PWM_OUTPUT)
     
    # set the PWM mode to milliseconds stype
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
     
    # divide down clock: Currently works at 50 Hz
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)
     
    delay_period = 0.01
 
    for pulse in range(50, 250, 1):
        #Take out of for loop if only wanting one position
        wiringpi.pwmWrite(PIN_NUMBA, pulse)
        time.sleep(delay_period)
    
# Return true if the difference between the GPS velocity measurements at different times
# have a difference within the GPS_DIFF_THRESHOLD (AKA velocity is more or less constant)
def gps_check():
    #GPS.get_velocity() to be implemented
    gps.update()
    veloc_init = gps.altitude_m
    time.sleep(SLEEP_TIME)
    veloc_after = gps.altitude_m
    if veloc_init == None or veloc_after == None:
        print("Was None")
        return False
    elif abs(veloc_init - veloc_after) < GPS_DIFF_THRESHOLD:
        print(veloc_init-veloc_after)
        return True
    return False

# # Will stall the program until the read acceleration is lower than the threshold
# def accel_check():
#     curChecks =0
#     # There must be a specified amount of consecutive successful acceleration checks
#     # before the program proceeds to secondary checks. This amount is specified by
#     #"CHECKS_NEEDED"
#     while (curChecks <= CHECKS_NEEDED):
#         if IMU.get_acceleration() >= ACCELERATION_THRESHOLD:
#             curChecks+= 1
#         else:
#             curChecks = 0
#         sleep(SLEEP_TIME)

# Script to be run when nose cap and drone cage have been released (i.e. after the 
# rocket has finished launching)
if __name__ == "__main__":
    
    checkCounter =0
    while (checkCounter <= CHECKS_NEEDED):
        if gps_check():
            checkCounter+= 1
        else:
            checkCounter = 0
        time.sleep(SLEEP_TIME)
    deploy()