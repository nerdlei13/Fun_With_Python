import socketserver

# simple server code below

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        
        self.data = self.request.recv(1024).strip()
        print("Received from {}:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 7070

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()
