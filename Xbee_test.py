from digi.xbee.devices import XBeeDevice

receiver = XBeeDevice("COM7", 9600)
receiver.open()
while(1):
    print(receiver.read_data())
receiver.close()