#Documentation: https://github.com/adafruit/Adafruit_CircuitPython_BNO055

#Library adafruit_bno055 must be pip installed on Raspberry Pi
import adafruit_bno055
from busio import I2C
from board import SDA, SCL

i2c = I2C(SCL, SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

# Accessible info: temperature, acceleration, magnetic, gyro, euler, quaternion, linear_acceleration, and gravity
# via sensor.____

# To calibrate/configure?  offsets_accelerometer, offsets_magnetometer, offsets_gyroscope, 
# radius_accelerometer, radius_magnetometer

# might not need?
def get_sensor():
    return sensor

def get_acceleration():
    return sensor.acceleration