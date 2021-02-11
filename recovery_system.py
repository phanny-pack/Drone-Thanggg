# Process Starts after x minutes of flight

# With GGA Output
# If (int(GPS Altitude) == Previous State)
#    if (Timer == 20 seconds)
#       Stop other functions();
#       Start Sending Data Through XBee();
#       break from loops
#    else
#       continue;
# Else
#    Previous State = GPS Altitude % 10
#    Reset Timer


# With RMC Output
# If (Velocity == 0)
#     Stop other functions
#     Start Sending Data Through XBee
#     break from loop
# Else
#    continue checking




#Reporting GPS to Terminal
# Import gpsd Library, Install From: https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/setting-everything-up
import gps
# Import Xbee Python Library, Install From: https://xbplib.readthedocs.io/en/latest/getting_started_with_xbee_python_library.html
from digi.xbee.devices import XBeeDevice
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
keepLooping = True

while keepLooping:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        if report['class'] == 'TPV':
            if hasattr(report, 'speed'):
                print(report.speed)
            if hasattr(report, 'lon'):
                print(report.lon)
            if hasattr(report, 'lat'):
                print(report.lat)
            if hasattr(report, 'alt'):
                print(report.alt)
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")

# XBee Device : DigiMeshDevice
# send_data_64(XBee64BitAddress, String or Bytearray, Integer)
## transceiver code: 

# Instantiate tranceiver Xbee device object
# Replace COM1 with XBee Device Port, usually starts with /dev/tty
device = XBeeDevice("COM1", 9600)
device.open()

# Instantiate a remote XBee device object.
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))

device.send_data_64(remote_device, "DATA")

## receiver code:

# Instantiate receiver Xbee device object
# Replace COM1 with XBee Device Port, usually starts with /dev/tty
device = XBeeDevice("COM1", 9600)
device.open()

# Instantiate a remote XBee device object.
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))

data_variable = device.read_data(remote_device)
# Take data and parse down to different variable for each attribute.

