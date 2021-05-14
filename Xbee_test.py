#!/usr/bin/env python
import time
import os
import serial

from digi.xbee.devices import XBeeDevice, DigiMeshDevice, RemoteXBeeDevice, XBee64BitAddress
os.system("sudo systemctl stop serial-getty@serial0.service")

# ser = serial.Serial(
#     port='/dev/serial0',
#     baudrate = 9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=1             
#  )
# counter=0  

# while 1:
#     #ser.write(str.encode('Write counter: %d \n'%(counter)))
#     #time.sleep(1)
#     #counter += 1
#     x=ser.readline().strip()
#     print(x)
#     if x == 'a':
#         # GPIO.output(23,GPIO.HIGH)
#         print("RECEIVED 'A'")
#         time.sleep(3)
#     # else:
#     #     # GPIO.output(23,GPIO.LOW)
#     #     print("...")

receiver = XBeeDevice("/dev/serial0", 9600)
# receiver.close()
receiver.open()
# receiver.set_sync_ops_timeout(10)
remote_device = RemoteXBeeDevice(receiver, XBee64BitAddress.from_hex_string("0013A20041C7BFD1"))
while(1):
    data_variable = receiver.read_data_from(remote_device)
    if(data_variable is None):
        print('No Data Found')
    else:
        print(data_variable.data.decode("utf-8"))
        print(data_variable.timestamp)
        print("============================")
        print()
    time.sleep(3)
receiver.close()

# import struct
# port = serial.Serial('/dev/serial0', baudrate=9600, rtscts=True, timeout=0.75)
# data_struct = struct.Struct('>BHBBBBBBBBBBBBBBBBBBHB')
# while True:
#   buf = port.read(24)
#   if len(buf) == 24:
#     frm = data_struct.unpack(buf)
#     if frm[0] == 0x7E:
#       print("Data packet is ",frm[1], "bytes long")
#       print("Analog measurement: ",frm[20]," (of 1023)")
# port.close