from digi.xbee.devices import XBeeDevice, XBee64BitAddress, RemoteXBeeDevice
import time

device = XBeeDevice("COM7", 9600)
device.open()
device.set_sync_ops_timeout(10)
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041C7BFFC"))
while(1):
    device.send_data(remote_device, "Data")
    print("sent")
    time.sleep(3)
device.close()