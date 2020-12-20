from socket import *
import struct, time
 
server = ("ipinfo.io",80)

client = socket( AF_INET, SOCK_STREAM)

client.connect(server)


client.send(b"GET / HTTP/1.1\r\nHost: ipinfo.io\r\n\r\n")

msg = client.recv(2048)

print(msg.decode())
