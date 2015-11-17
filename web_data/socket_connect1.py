import socket 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

print "connecting..."

times = 0
while True:
    print "hit loop {} times".format(times)
    data = mysock.recv(512)
    if (len(data) < 1 ):
        break
    print data
    times += 1
mysock.close()
