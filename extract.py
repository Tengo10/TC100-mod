import serial
import sys
import time

if len(sys.argv) == 1:
    print("usage: extract.py 'port' 'filename'")
    sys.exit()

comPort = sys.argv[1]

filename = sys.argv[2]

ser = serial.Serial()

ser.port = comPort
ser.baudrate = 115200
ser.open()

if ser.is_open:
    print("COM: ", comPort, " open!")
    print("waiting for device...")
else:
    print("TTY: ", comPort, " not found")
    sys.exit()

line = ser.readline()
while line != b'Hit any key to stop autoboot:  1 \r\n':
    line = ser.readline()
    #print(line)
print("Camera found, booting into Uboot!")
time.sleep(0.2)
ser.write(b'a\r\n')
time.sleep(0.2)
print("Initializing flash")
ser.write(b'sf probe 0\r\n')
time.sleep(2)
print("Copying partitions to RAM")
ser.write(b'sf read 0x82000000 0x0 0x7EE000\r\n')
time.sleep(7)
print("Writing RAM to SD Card")
out = bytes(('fatwrite mmc 0 0x82000000 ' + filename + ' 0x7EE000\r\n'), "ascii")
ser.write(out)
time.sleep(10)
print("Done!")
sys.exit
