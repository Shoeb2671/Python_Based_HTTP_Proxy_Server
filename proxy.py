from socket import *
from ResponseManager import*




class PythonProxyServer:
    def __init__(self,port):
        self.ip = '0.0.0.0'
        self.port=port
        self.http_header = "HTTP/1.1 200 OK\n\n"
        self.socket = socket(AF_INET,SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.socket.bind((self.ip,self.port))
        self.responseManager = ResponseManager()

    def listen(self,backlog):
        self.socket.listen(backlog)
        print("Proxy Server started on port "+str(self.port))

    def accept(self):
        self.socket.accept()
        self.responseWriter,self.clientAddr = self.socket.accept()
        self.requestStr = self.responseWriter.recv(1024).decode()
        print(self.requestStr)
        msg = self.responseManager.getBlockedWebsitePage()
        self.responseWriter.sendall(msg.encode("utf-8"))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

     while True:
        proxy = PythonProxyServer(2647);
        proxy.listen(5)
        proxy.accept()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
