# UART Control
#
# This example shows how to use the serial port on your OpenMV Cam. Attach pin
# P4 to the serial input of a serial LCD screen to see "Hello World!" printed
# on the serial LCD display.

import time
from pyb import UART

# Always pass UART 3 for the UART number for your OpenMV Cam.
# The second argument is the UART baud rate. For a more advanced UART control
# example see the BLE-Shield driver.
uart = UART(3, 9600)

# while(True):
#uart.write("\n")
uart.write("AT+RST\r\n")
#uart.write("\n")
#time.sleep(10)
s = "s"
while(True):
    if(uart.any()>0):
        s = uart.readall()
        print(s)
        print(s.decode('utf-8'))#字节转字符串
