import os

from digi.xbee.devices import XBeeDevice, DigiMeshDevice, RemoteXBeeDevice
os.system("sudo systemctl stop serial-getty@serial0.service")

receiver = XBeeDevice("/dev/serial0", 9600)
receiver.close()
receiver.open()
while(1):
    print(receiver.read_data())
receiver.close()