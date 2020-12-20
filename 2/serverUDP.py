from socket import *

a = []
des_ip = '127.0.0.1'
des_port = 1234 
s = socket(AF_INET,SOCK_DGRAM) 
s.bind((des_ip,des_port))
while True:
    client, addr = s.recvfrom(1024)
    if(client.decode() == "GET"):
        s.sendto(str(len(a)).encode(),addr)
        if len(a)==0:
            pass
        else:
            for i in range(0,len(a)):
                s.sendto(str(a[i]).encode(),addr)
        
    elif("POST" in client.decode()):
        client = client.decode()
        client = client [5:]
        a.append([addr[0],addr[1],client])
        print("NEW POST")
    elif(client.decode() == "DELETE"):
        n_o_p = []
        for i in range(0,len(a)):
                if (a[i][0] == addr[0]):
                    n_o_p.append(i)
        for i in range(len(n_o_p)-1 ,-1,-1):
            a.pop(i)

           