import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode("utf-8")
        # self.dataself.data.decode("utf-8")
        print(f"{self.client_address[0]} wrote:")
        print(self.data)
        if self.data == "cat" or self.data == "dog":
            image = open(f'{self.data}.png', 'rb')
            image_data = image.read()
            image.close()
            message = image_data
        else:
            # Send back custom message
            message = input("Type message: ")
            message = bytes(message, "utf-8")
        self.request.sendall(message)


def main():
    HOST, PORT = "192.168.0.3", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

if __name__ == '__main__':
    main()
