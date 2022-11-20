import serial, time
ser = serial.Serial("COM5", 9600, timeout=1)
while True:

    ser.write(b"P")
    time.sleep(2)
    ser.write(b"N")
    time.sleep(2)
    ser.write(b"P")
