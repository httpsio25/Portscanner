# this is a simple port scanner that evaluates whether a port is open by whether we can create a socket at the port
import socket
import sys

# this is our first function!
print("[*]This tool was created by Israel"
def checkports(ip,portlist):
    try:
        for port in portlist:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result=sock.connect_ex((ip,port))
            if result==0:
                print('Port {}: \t Open'.format(port))
            else:
                print('Port {}: \t Closed'.format(port))
            sock.close()

    except socket.error as error:
        print(str(error))
        print('Connection Error')
        sys.exit()

# this calls our function checkports and passes parameters to it with IP and ports
checkports("192.168.100.5",[21,22,25,80,81,443])
