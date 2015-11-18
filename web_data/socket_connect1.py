import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.settimeout(10)
# print socket.getaddrinfo('www.py4inf.com', 80, 0, 0, socket.IPPROTO_TCP)
mysock.connect(('bpa.indemand.com', 80))
mysock.send('GET http://bpa.indemand.com HTTP/1.0\n\n')

print "connecting..."

# data = mysock.recv(512)
#
# print data

for n in range(20):
    print "hit loop {} times".format(n)
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data;
mysock.close()
