from digi.xbee.devices import XBeeDevice, XBee64BitAddress, RemoteXBeeDevice

device = XBeeDevice("COM7", 9600)
device.open()
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))
while(1):
    device.send_data(remote_device, "Data")
    print("sent")
device.close()