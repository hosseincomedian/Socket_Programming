from socket import *
import struct, time
 
server = ("pool.ntp.org",123)
msg = '\x1b' + 47 * '\0'

time1970 = 2208988800 #1970

client = socket( AF_INET, SOCK_DGRAM)
client.sendto(msg.encode('utf-8'), server)
msg, server = client.recvfrom(1024)
t = struct.unpack( "!12I", msg )[10]
t -= time1970
t= time.ctime(t).replace("  "," ")
print (t)