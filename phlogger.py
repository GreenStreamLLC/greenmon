#!/usr/bin/python

import datetime
import serial

# Serial code adapted from: https://www.atlas-scientific.com/_files/code/pi_sample_code.pdf
usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 38400)
# turn on the LEDs
ser.write("L1\r")
ser.write("C\r")
line = ""
while True:
    data = ser.read()
    if(data == "\r"):
        print "Received from sensor:" + line
        # Parse the data
        try:
            line = float(line)
        except:
            print "Couldn't parse float: ", line
            continue
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        
    else:
        line = line + data 
while True:
    #Open Log File
    f = open('pHlog.txt','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M")
    outvalue = temperature()
    outstring = str(timestamp)+"  "+str(outvalue)+" C "+str(outvalue*1.8+32)+" F"+"\n"
    print outstring
    f.write(outstring)
    f.close()

    #log pH every 60 seconds
    time.sleep(60)