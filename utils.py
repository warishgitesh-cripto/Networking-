import socket


def get_local_ip():
    """Returns the local IP address of the machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))  
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  # Assume localhost
    finally:
        s.close()
    return ip


def check_port_open(host, port):
    """Returns True if the port is open, False otherwise."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    try:
        sock.connect((host, port))
    except (socket.timeout, socket.error):
        return False
    finally:
        sock.close()
    return True


def ping(host):
    """Pings a host to check if it's reachable."""
    response = os.system("ping -c 1 " + host)
    return response == 0
