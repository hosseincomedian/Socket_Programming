from socket import *
import time

des_ip = '127.0.0.1'
des_port = 12345 
s = socket(AF_INET,SOCK_STREAM) #AF_INET : IPV4 , SOCK_STREAM:TCP+++
s.connect((des_ip,des_port))

while True:
    data = input('shoma:  ')
    s.send(data.encode())
    if data =='Good Bye':
        print('end...')
        break 
    data2 = s.recv(1024)
    print('server:  ' ,data2.decode())
    if data2.decode() =='Good Bye':
        print('end...')
        break

s.close()
