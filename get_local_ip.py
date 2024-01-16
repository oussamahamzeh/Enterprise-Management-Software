import socket
from datetime import datetime
import sys

def get_local_ip():
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        quit_command = "CTRL-C" if sys.platform == "win32" else "CONTROL-C"
        default_port = "8000"
        protocol = "http"
        localhost = '127.0.0.1'
        now = datetime.now().strftime("%B %d, %Y - %X")
        print(
            f"{now}\n\n"
            f"To reach the server Locally go to: {protocol}://{localhost}:{default_port}/\n\n"
            f"To reach the server Remotely go to: {protocol}://{local_ip}:{default_port}/\n\n"
            f"Quit the server with {quit_command}.\n\n"
        )
        return local_ip
    except socket.error:
        print("Unable to get the IP")
        return '127.0.0.1'

if __name__ == "__main__":
    get_local_ip()
