import http.server
import socketserver
import time

PORT = 8000
FILE_PATH = '/git_graph.txt'
TIMEOUT = 10  # in seconds


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = FILE_PATH
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


def run_server(timeout=TIMEOUT, port=PORT, forever=False):
    """Runs the serve at localhost:<port> for <timeout> seconds. If <forever> is True, then the server will run forever.

    Args:
        timeout (int, optional): Defaults to TIMEOUT=10 s.
        port (int, optional): Defaults to PORT=8000.
        forever (bool, optional): defaults to False.
    """
    handler = CustomHandler

    httpd = socketserver.TCPServer(("", PORT), handler)
    print("serving at ", f"http://localhost:{PORT}/")

    start_time = time.time()
    while time.time() - start_time < TIMEOUT:
        httpd.handle_request()

    httpd.server_close()