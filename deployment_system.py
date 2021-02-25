from data_logging import IMU_logging
import time

ACCELERATION_THRESHOLD = 1 # in m/s^2
SLEEP_TIME = 0.1 # in seconds
CHECKS_NEEDED = 5

IMU_SENSOR = IMU_logging.getSensor()

def deploy():
    return
    #whatever is needed. Send a signal to the motor?
    
# Return true if the GPS is changing at a constant rate
def gps_check():
    # Uses the velocity attribute? is equivalent to the past velocity measurement +-
    # the acceleration threshold
    return 

# Will stall the program until the read acceleration is lower than the threshold
def accel_check():
    curChecks =0
    # There must be a specified amount of consecutive successful acceleration checks
    # before the program proceeds to secondary checks. This amount is specified by
    #"CHECKS_NEEDED" 
    while (curChecks <= CHECKS_NEEDED):
        if IMU_SENSOR.acceleration >= ACCELERATION_THRESHOLD:
            curChecks+= 1
        else:
            curChecks = 0
        sleep(SLEEP_TIME)

# Script to be run when nose cap and drone cage have been released (i.e. after the 
# rocket has finished launching)
if __name__ == "__main__":
    atTermVel = False
    while (not atTermVel):
        accel_check()
        atTermVel = gps_check()
        
    deploy()