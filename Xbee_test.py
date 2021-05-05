import os
# import serial

from digi.xbee.devices import XBeeDevice, DigiMeshDevice, RemoteXBeeDevice
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
#     if x == '61':
#         # GPIO.output(23,GPIO.HIGH)
#         print("RECEIVED 'A'")
#         time.sleep(3)
#     # else:
#     #     # GPIO.output(23,GPIO.LOW)
#     #     print("...")

receiver = XBeeDevice("/dev/serial0", 9600)
# receiver.close()
receiver.open()
while(1):
    print(receiver.read_data())
receiver.close()