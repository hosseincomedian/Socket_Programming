from socket import *
from _thread import *

my_ip = '127.0.0.1'
my_port = 12345 
count = []
s = socket(AF_INET,SOCK_STREAM)
s.bind((my_ip,my_port))
s.listen(5)

def multi_threaded_client(connection,count):
    # print('count darooni while:',count)
    if len(count) >=5:
        print(len(count))
        data = connection.recv(2048)
        data = connection.recv(2048)
        data = connection.recv(2048)
        data = 'Server Is Busy'
        connection.send(data.encode())
        

            
    else:
        while True:
            print(len(count))
            # print('count darooni while:',count)
            a=[]
            data = connection.recv(2048)
            if ((data.decode())=='end'):
                count.pop()
                break
            else:
                a.append(int(data))
                data = connection.recv(2048)
                a.append(int(data))
                data = connection.recv(2048)
                a.append(int(data))
                a.sort()
                data = str(a[1])
                connection.send(str(a[1]).encode())
                print(a)

        connection.close()
        

while True:
    Client, address = s.accept()
    count.append(Client)
    print('ghabl')
    start_new_thread(multi_threaded_client, (Client,count, ))
    print('bad')
    



  