import socket
import threading
import argparse


def connect_to_server(port=4444):
    """

    :param clientToServeSocket:
    :param clientIPAddress:
    :param portNumber:
    :return:
    """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', port)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:
        # Send data
        message = b'This is the message.  It will be repeated.'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()


def startServer(portNumber):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", portNumber))
    server.listen(10)
    print("[!] Listening locally on port %d ..." % portNumber)

    while True:
        client, address = server.accept()
        print("[+] Connected with the client: %s:%d" % (address[0], address[1]))

        #Handle clients through multi-threading
        serveClientThread = threading.Thread(target=serveClient, args=(client, address[0], address[1]))
        serveClientThread.start()

def main():
    """

    :return:
    """
     # Parse the command line arguments
    parser = argparse.ArgumentParser('TCP server')
    parser.add_argument("-p", "--port", type=int, help="The port number to connect with", default=4444)
    args = parser.parse_args()

    # Store the argument value
    portNumber = args.port
    
    connect_to_server(portNumber)


if __name__ == "__main__":
    main()