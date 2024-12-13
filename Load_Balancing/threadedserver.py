import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        curr_thread = threading.current_thread()
        response = bytes("{}: {}".format(curr_thread.name, data), 'ascii')
        self.request.sendall(response)
    
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))


if __name__ == "__main__":
    HOST, PORT = "localhost", 7070
    #HOST2, PORT2

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
  
    with server:
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread loop running in thread: ", server_thread.name)

        client(ip, port, "Response 1")
        client(ip, port, "Response 2")
        client(ip, port, "Response 3")
        client(ip, port, "Response 4")
        # next steps, have each thread sleep then process a new request
        # could use a queue
        server.shutdown()