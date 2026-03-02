import socket

class NetworkingApp:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.sock = self.create_socket()

    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        print(f'Server listening on {self.host}:{self.port}')
        return sock

    def start(self):
        while True:
            client, address = self.sock.accept()
            print(f'Connection from {address} established.\n')
            client.close()

if __name__ == '__main__':
    app = NetworkingApp()
    app.start()