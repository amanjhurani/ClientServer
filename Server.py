import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    a = clientsocket.recv(1024)
    a = a.decode("utf-8")
    a = str(a).upper()
    # print(f"Connection from {address} has been established!")
    clientsocket.send(bytes(a,"utf-8"))
    if str(a) == "BREAK":
        exit()
    print("Message sended Successfully :" + a)
    clientsocket.close()
