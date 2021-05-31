import serial
import sys
import time

############################
#                          #
#       Broken ATM         #
#                          #
############################


if len(sys.argv) == 1:
    print("usage: extract.py 'port' 'password'")
    sys.exit()

comPort = sys.argv[1]

pw = sys.argv[2]

ser = serial.Serial()

ser.port = comPort
ser.baudrate = 115200
ser.open()

if ser.is_open:
    print("COM: ", comPort, " open!")
    print("Waiting for device...")
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
ser.write(b'env set bootargs console=ttySAK0,115200n8 root=/dev/mtdblock4 rootfstype=squashfs init=/bin/sh mem=64M memsize=64M\r\n')
time.sleep(0.2)
ser.write(b'env save\r\n n')
time.sleep(0.2)
ser.write(b'reset \r\n')
print("Uboot env changed, restarting...")
time.sleep(15)
print("Initializing Linux")
ser.write(b'./etc/init.d/rcS')
time.sleep(15)
ser.write(b'passwd root')
time.sleep(0.5)
ser.write(bytes(pw, 'ascii') + b'\r\n')
time.sleep(0.5)
ser.write(bytes(pw, 'ascii') + b'\r\n')
print("Password set, booting to Uboot...")
ser.write(b'reboot -f \r\n')

line = ser.readline()
while line != b'Hit any key to stop autoboot:  1 \r\n':
    line = ser.readline()
print("Camera found, booting into Uboot!")
time.sleep(0.2)
ser.write(b'a\r\n')
time.sleep(0.2)
ser.write(b'env set bootargs console=ttySAK0,115200n8 root=/dev/mtdblock4 rootfstype=squashfs init=/sbin/init mem=64M memsize=64M\r\n')
time.sleep(0.2)
ser.write(b'env save\r\n')
time.sleep(0.2)
ser.write(b'reset \r\n')
#ser.write(b'env set bootargs console=ttySAK0,115200n8 root=/dev/mtdblock4 rootfstype=squashfs init=/sbin/init mem=64M memsize=64M\r\n')