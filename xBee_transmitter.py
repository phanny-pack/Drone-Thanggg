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

device = XBeeDevice("COM7", 9600)
device.open()
device.set_sync_ops_timeout(10)
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041C7BFFC"))


while keepLooping:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current drone's info
        if report['class'] == 'TPV':
            # checks if each attribute is available and records data in a variable
            if hasattr(report, 'speed'):
                velocity = report.speed
                print(report.speed)
            if hasattr(report, 'lon'):
                longitude = report.lon
                print(report.lon)
            if hasattr(report, 'lat'):
                latitude = report.lat
                print(report.lat)
            if hasattr(report, 'alt'):
                altitude = report.alt
                print(report.alt)
        
        # Sends data as a string over to receiver xbee
        device.send_data(remote_device, longitude + "," + latitude + "," + altitude + "," + velocity)
        time.sleep(3)

    except KeyError:
        pass
    except StopIteration:
        session = None
        print("GPSD has terminated")