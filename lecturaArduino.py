import serial, time
arduino=serial.Serial("COM8",9600)
time.sleep(2)
while True:
    valor=int(arduino.readline().decode("ascii"))
    if(valor<400):
        print("es de noche")
    else:
        print("es de día")
    print(valor)
