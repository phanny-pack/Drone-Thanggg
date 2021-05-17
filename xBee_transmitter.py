# Drone Code
#
#
import gps
import time
# Import Xbee Python Library, Install From: https://xbplib.readthedocs.io/en/latest/getting_started_with_xbee_python_library.html
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
keepLooping = True

xBeeLocation = "COM7"
device = XBeeDevice(xBeeLocation, 9600)
device.open()
device.set_sync_ops_timeout(10)
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041C7BFFC"))

# Placeholder Data Format: longitude + "," + latitude + "," + altitude + "," + velocity

while keepLooping:
    
    # Sends data as a string over to receiver xbee
    device.send_data(remote_device, #TODO: DATA GOES HERE
                        )
    time.sleep(3)
    