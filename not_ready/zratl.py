import socket
class module:
  def __init__(self):
    self.listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.name = 'zRAT listener'
    self.PORT = 8000
    self.help = 'PORT: The port to listen for connections'
  def main(self):
    print('MAIN')
