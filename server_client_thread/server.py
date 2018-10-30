import socket
from threading import Thread, currentThread


class ServerThread(Thread):

    def __init__(self, threadName, serverName):
        Thread.__init__(self, name=threadName)
        self.server = serverName

    def run(self):
        while True:
            print('对方发送的消息:', self.server.recv(1024).decode('utf-8'))
            accept = AcceptThread(currentThread().getName(), self.server)
            accept.start()


class AcceptThread(Thread):
    def __init__(self, threadName, serverNames):
        Thread.__init__(self, name=threadName)
        self.serverNames = serverNames

    def run(self):
        while True:
            str1 = input('输入发送的消息:\n')
            self.serverNames.sendall(str1.encode('utf-8'))


server = socket.socket()
host = socket.gethostname()
port = 8888
server.bind((host, port))
server.listen(5)
print('server waiting ......')
conn, adds = server.accept()
print('等待对方发送消息')
Li = ServerThread('Li', conn)
Li.start()
