from socket import *
import time



            

my_ip = '127.0.0.1'
my_port = 12345 

count = []
s = socket(AF_INET,SOCK_STREAM)  
s.bind((my_ip,my_port))

s.listen(1)
while True:  
    Client, address = s.accept()
    count.append(Client)
    while True:
        try:   
            data = Client.recv(1024)
            print('client:  ' ,data.decode())
            if ((data.decode())=='Good Bye'):
                print('end...')
                break
            else:
                data = input("shoma:    ")
                Client.send(data.encode())
                if data =='Good Bye':
                    print('end...')
                    break
                data = data.encode()
        except :
            print('motavajeh nashodam client chi goft')
            data = "mishe dobare tekrar konid?"
            data = data.encode()
            Client.send(data)
    Client.close()
  





  