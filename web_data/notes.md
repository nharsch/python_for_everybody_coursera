# Week 2

## Regex

# Week 3

## 04.01 Networked Programs

### Sockets

**Socket** best thought of as a connection we don't worry about. 
Endpoint of a bidirectional inter-process communication glow
across an IP based computer network, such as the internet

TCP **Port** numbers - point of contact from clients and applications running 
on server

Python has built-in support for TCP sockets

    import socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect( ('www.py4inf.com', 80) )


## 04.02 From Sockets to Applications

HTTP is the most dominent Application protocol on the internet. Works like
this:

* client asks server for document
* client waits for response
* server returns response, connection is closed

*URL* Uniform resource locator. Protocol 'http://'- Host 'nyt.com' - document '/today'

### Telnet - Hacking HTTP

    telnet <HOST> <PORT>
    > GET <document> <PROTOCOL> HTTP/1.0

During a web page lookkup, several GET requests usually fire. CSS, JS, external
resources, etc.

## 04.03 Writing a web browser

with socket. Not working at office.

with urllib. Urllib makes URLs more like files 


