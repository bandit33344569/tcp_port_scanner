from socket import *
import threading
import argparse


def scan_TCP_port(ip, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        print(f"TCP Port: {port} Open")
    except:
        print(f"TCP Port: {port} CLOSED")


def check(ip, ports):
    for port in ports:
        thread = threading.Thread(target=scan_TCP_port, args=(ip, int(port)))
        thread.start()


def main():
    print("Welcome To Port Scanner!\n")
    try:
        parser = argparse.ArgumentParser("Ports Scanner")
        parser.add_argument("-a", "--address", type=str, help="Enter the ip address to scan")
        parser.add_argument("-p", "--port", type=str, help="Enter The ports to scan")
        args = parser.parse_args()
        ip = args.address
        port = args.port.split(',')
        #port = [ p for p in range(1, 100)]
        check(ip, port)
    except:
        print("format error\n example: python scan.py -a 127.0.0.1 -p 21,22,80")


if __name__ == "__main__":
    main()
