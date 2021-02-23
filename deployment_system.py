from data_logging import IMU_logging
import time

ACCELERATION_THRESHOLD = 1 # in m/s^2
SLEEP_TIME = 0.1 # in seconds

sensor = IMU_logging.getSensor()

atTermVel = False
while (not atTermVel):
    accel_check()
    atTermVel = gps_check()
    
deploy()

def deploy():
    return
    #whatever is needed
    
# Return true if the GPS is changing at a constant rate
def gps_check():
    return 

# Will stall the program until the read acceleration is lower than the threshold
def accel_check():
    while (sensor.acceleration >= ACCELERATION_THRESHOLD):
        sleep(SLEEP_TIME)