from digi.xbee.devices import XBeeDevice

device = XBeeDevice("COM7", 9600)
device.open()
while(1):
    device.send_data_broadcast("DATA")
    print("sent")
device.close()