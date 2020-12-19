from socket import *


des_ip = '127.0.0.1'
des_port = 12345 
s = socket(AF_INET,SOCK_STREAM) #AF_INET : IPV4 , SOCK_STREAM:TCP+++
s.connect((des_ip,des_port))

while True:
    data = input('1: ')
    s.send(data.encode())
    if data =='end':
        break

    data = input('2: ')
    s.send(data.encode())
    if data =='end':
        break
    
    
    data = input('3: ')
    s.send(data.encode())
    if data =='end':
        break
    
    
    data2 = s.recv(1024)
    print(data2.decode())

s.close()
