from socket import *

des_ip = '127.0.0.1'
des_port = 1234 
s = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('msg:  ')
    data = data.encode()
    s.sendto(data,(des_ip,des_port))
    data = data.decode()
    if(data == "GET"):
        number = s.recv(1024)
        number = int(number.decode())
        if (number == 0):
            print('empty...')
        else:
            for i in range(0,number):
                msg = s.recv(1024)
                print(msg.decode())       
    else:
        pass
