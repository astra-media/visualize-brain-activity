import socket
import msvcrt

UDP_IP = "127.0.0.1"
UDP_PORT = 5007

while True:

    input_char = msvcrt.getch()

    if input_char.upper() == 'W':
        MESSAGE = "Pushing"
        print 'Pushing'
    elif input_char.upper() == 'S':
        MESSAGE = 'Pulling'
        print "Pulling"


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
