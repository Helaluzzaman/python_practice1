import socket
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("data.pr4e.org", 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
c.send(cmd)

while True:
    data = c.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
c.close