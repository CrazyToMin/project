import socket
from threading import Thread, currentThread


class ClientThreading(Thread):
    def __init__(self, threadName, user):
        Thread.__init__(self, name=threadName)
        self.user = user

    def run(self):
        while True:
            str1 = input('请输入发送的消息:\n')
            self.user.sendall(str1.encode('utf-8'))
            accept = AcceptThread(currentThread().getName(), self.user)
            accept.start()


class AcceptThread(Thread):
    def __init__(self, threadName, user):
        Thread.__init__(self, name=threadName)
        self.user = user

    def run(self):
        print('接受的消息:', self.user.recv(1024).decode('utf-8'))


client = socket.socket()
host = socket.gethostname()
client.connect((host, 8888))
use = ClientThreading('liu', client)
use.start()
# print('接受的消息:', client.recv(1024).decode('utf-8'))
