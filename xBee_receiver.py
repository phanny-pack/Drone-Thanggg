# Receiver Code
import gps
import time
# Import Xbee Python Library, Install From: https://xbplib.readthedocs.io/en/latest/getting_started_with_xbee_python_library.html
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
#
#
# Instantiate receiver Xbee device object
# Replace COM1 with XBee Device Port, usually starts with /dev/tty
receiver = XBeeDevice("/dev/serial0", 9600)
receiver.open()

# Instantiate a remote XBee device object.
remote_device = RemoteXBeeDevice(receiver, XBee64BitAddress.from_hex_string("0013A20041C7BFD1"))


# Take data and parse down to different variable for each attribute.
while(True):
    data_variable = receiver.read_data(remote_device)
    if(data_variable is None):
        print('No Data Found')
    else:
        dataString = data_variable.data.decode("utf-8")
        attributes = dataString.split(",")
        longitude = float(attributes[0])
        latitude = float(attributes[1])
        altitude = float(attributes[2])
        velocity = float(attributes[3])
        time.sleep(3)

receiver.close()

# Datalogging can be done here