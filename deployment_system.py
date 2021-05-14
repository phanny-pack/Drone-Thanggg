from data_logging import IMU_Logging as IMU
from data_logging import recovery_system as GPS
import time
#pip install wiringpi
import wiringpi

ACCELERATION_THRESHOLD = 1 # in m/s^2
GPS_DIFF_THRESHOLD =  0.5 # in m/s
SLEEP_TIME = 0.1 # in seconds
CHECKS_NEEDED = 5
gps = adafruit_gps.GPS(uart, debug=False) # Use UART/pyserial

def deploy():
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
    veloc_init = gps.speed_knots
    time.sleep(SLEEP_TIME)
    veloc_after = gps.speed_knots
    if abs(veloc_init - veloc_after) < GPS_DIFF_THRESHOLD:
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

    atTermVel = False
    while (not atTermVel):
        # accel_check()
        atTermVel = gps_check()
    deploy()