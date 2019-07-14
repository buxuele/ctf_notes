# Time: 2019/05/02 12:24 AM
# About: python3 socket port scan on localhost

import socket


def try_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    try:
        s.connect(("127.0.0.1", port))
    except socket.error:
        # print("This Post is closed")
        return False

    try:
        s.send(b"hi")
        data = s.recv(4096)
        print(data)
        s.close()
        print("this Port is Open")
        return True
    except socket.timeout:
        print("port is open, but timeout!")
        s.close()
        return True


def scan():
    found_ports = []
    for port in range(1, 65535):
        connected = try_port(port)
        if connected:
            found_ports.append(port)
    return found_ports


print(scan())






































