import argparse
# from socket import *
from socket import AF_INET, SOCK_STREAM, socket, gethostbyname, gethostbyaddr, setdefaulttimeout
import sys

# Usage: #python  PortScanner.py -a 206.189.185.57 -p 21,80


def print_banner(connSock=None, tgtPort=None):
    """
    
    :param connSock:
    :param tgtPort:
    :return:
    """
    try:
        # Send data to target
        if tgtPort == 80:
            request = b"GET / HTTP/1.1\nHost: www.globalshop.co.il\n\n"
            connSock.send(request)
            # request = "GET / HTTP/1.1"
            # connSock.send(request.encode())
        else:
            connSock.send("\r\n")

        # Receive data from target
        results = connSock.recv(4096)
        # print the banner
        print('[+] Banner:' + str(results))
    except Exception as e:
        print('[-] Banner not available\n')


def conn_scan(tgtHost, tgtPort):
    try:
        # Create the socket object
        connSock = socket(AF_INET, SOCK_STREAM)
        # try to connect with the target
        connSock.connect((tgtHost, tgtPort))
        print('[+] %d tcp open' % tgtPort)
        print_banner(connSock, tgtPort)
    except Exception as e:
        # Print the failure results
        print('[+] %d tcp closed' % tgtPort)
    finally:
        # close the socket object
        connSock.close()


def portScan(tgtHost,tgtPorts):
    """

    :param tgtIp:
    :param tgtPorts:
    :return:
    """
    try:
        # if -a was not an IP address this will resolve it to an IP/ if it's an IP
        # that's fine it will return the same IP
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Error: Unknown Host")
        sys.exit()

    try:
        # if the domain can be resolved that's good, the results will be
        # something like: ('domain.com', [], ['20.13.64.15'])
        tgtName = gethostbyaddr(tgtIP)
        print("[+]--- Scan result for: " + tgtName[0] + " ---")
    except:
        print("[+]--- Scan result for: " + tgtIP + " ---")

    setdefaulttimeout(10)

    # For each port number call the connScan function
    for tgtPort in tgtPorts:
        conn_scan(tgtHost, int(tgtPort))


def main():
    """

    :return:
    """
    # Parse the command line arguments
    parser = argparse.ArgumentParser('Smart TCP Client Scanner')
    parser.add_argument("-a", "--address", type=str, help="The target IP address")
    parser.add_argument("-p", "--port", type=str, help="The port number to connect with")
    args = parser.parse_args()

    # Store the arguments values
    ipaddress = args.address
    portNumbers = args.port.split(',')

    #Call the Port Scan function
    portScan(ipaddress, portNumbers)


if __name__ == "__main__":
    # Call the main function
    main()
