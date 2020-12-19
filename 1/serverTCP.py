from socket import *
from _thread import *



def multi_threaded_client(connection,count):
    # print('count darooni while:',count)
    if len(count) >= 5:
        
        data = 'Server Is Busy'
        connection.send(data.encode())
        count.pop()
            
    else:
        while True:
            
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
        connection.close()
  
my_ip = '127.0.0.1'
my_port = 12345 

count = []
s = socket(AF_INET,SOCK_STREAM) # i.  AF_INET6 "IPV6"  
s.bind((my_ip,my_port))

s.listen(1)
while True:
    Client, address = s.accept()
    count.append(Client)
    #iii . Client.settimeout(10)
    start_new_thread(multi_threaded_client, (Client,count, ))



#ii.
    #import select
    # servers = []
    # count = []
    # s1 = socket(AF_INET, SOCK_STREAM)
    # s1.bind(("127.0.0.1", 12345))
    # s1.listen(1)
    # servers.append(s1)

    # s2 = socket(AF_INET, SOCK_STREAM)
    # s2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # s2.bind(("127.0.0.1", 12346))
    # s2.listen(1)
    # s2.append(s2)

    # while True:
    #     readable, empty, empt = select.select(servers, [], [])
    #     ready_server = readable[0]
    #     Client, addr = ready_server.accept()   
    #  count.append(Client)
    #  start_new_thread(multi_threaded_client, (Client,count, ))
    



  