import socket, serial, time
group = '224.0.0.1'
port = 5004
arduino=serial.Serial("COM6",9600)
time.sleep(1)
# 2-hop restriction in network
ttl = 2
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)
sock.sendto(b"hello world", (group, port))
while True:
    valor=int(arduino.readline().decode("ascii"))
    if(valor<400):
        message="P"
        print("es de noche")
        sock.sendto(message.encode("utf-8"), (group, port))
    else:
        print("es de día")
        message="N"
        sock.sendto("N".encode("utf-8"), (group, port))
