import socket

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 8080))
        receiving_file = open(r'C:\Users\User\PycharmProjects\GamblingSim\epiclbdata.txt', 'wb')
        filedata = s.recv(1024)
        receiving_file.write(filedata)
    except:
        pass
