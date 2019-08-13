import socket
connect = True
while connect:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    msgs = input("Enter a Message to send to Server : ")
    s.send(bytes(msgs,"utf-8"))
    msg = s.recv(1024)
    msg = msg.decode("utf-8")
    if msg == "BREAK":
        connect = False
    print(msg)
    s.close()
