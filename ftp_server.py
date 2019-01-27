import socket
import threading
from tools import get_logger

FTP_ROOT_DIR = "/mnt/d/ftp_test"

logger = get_logger()


class FTPHandler(threading.Thread):
    pasv_mode: bool = False
    data_sock_addr: str = None
    data_sock_port: int = None

    def __init__(self, client_sock: socket.socket, client_address: tuple):
        self.route = {
            "port": self.handle_port,
            "pwd": self.handle_pwd,
            "user": self.handle_user,
            "type": self.handle_type
        }
        self.client_sock = client_sock
        self.client_host = client_address[0]
        self.client_port = client_address[1]
        super().__init__()

    def run(self):
        self.send("220 Welcome")
        while True:
            try:
                request = self.client_sock.recv(1024).rstrip().decode("utf-8")
                self.log("request: " + request)
                try:
                    cmd, args = request[:4].strip().lower(), request[4:].strip() or None
                    if args:
                        self.route[cmd](args)
                    else:
                        self.route[cmd]()
                except KeyError:
                    self.send("502 Unsupported")
            except socket.error as e:
                if e.errno == 32:
                    # Broken pipe
                    self.log("Connection disconnected: Broken pipe")
                    break
                raise e

    def handle_list(self):
        pass


    def handle_port(self, args: str):
        if self.pasv_mode:
            self.send("502 Unsupported PASV Model")
        else:
            data = args.split(",")
            self.data_sock_addr = ".".join(data[:4])
            self.data_sock_port = (int(data[4])<<8)+int(data[5])
            self.send("200 Get port")

    def handle_pwd(self):
        self.send("257 /")

    def handle_user(self, args: str):
        username = args
        if username and username == "anonymous":
            self.send("230 Login Success")
        else:
            self.send("530 only support anonymous user")

    def handle_type(self, args: str):
        # Only Support binary mode
        if args == "I":
            self.send("200 binary mode")
        else:
            self.send("502 unsupported translate model")

    def send(self, response: str):
        self.client_sock.send(f"{response}\r\n".encode("utf-8"))
        self.log("response: " + response)

    def log(self, string: str):
        logger.info(f"%-20s | %s" % (f"{self.client_host}:{self.client_port}", string))


class BasicFTPServer(object):

    def __init__(self, host: str = "127.0.0.1", port: int = 8020):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(5)

        logger.info(f"FTP server started, listen on {host}:{port}")

    def run(self):
        while True:
            connection, address = self.sock.accept()
            client_host: str = address[0]
            client_port: int = address[1]
            logger.info(f"%-20s | Created a new connection" % f"{client_host}:{client_port}")

            conn = FTPHandler(connection, address)
            conn.run()


if __name__ == "__main__":
    BasicFTPServer().run()
