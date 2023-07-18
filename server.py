import http.server
import socketserver
import threading
import time

PORT = 8000
FILE_PATH = '/git_graph.txt'
TIMEOUT = 10  # in seconds


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = FILE_PATH
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


def _run_server(timeout, port, forever):
    """Runs the serve at localhost:<port> for <timeout> seconds. If <forever> is True, then the server will run forever.
    To be run on a separate thread by start_server.
    """
    handler = CustomHandler

    httpd = socketserver.TCPServer(("", port), handler)
    print("serving at ", f"http://localhost:{port}/")

    start_time = time.time()
    while time.time() - start_time < timeout:
        httpd.handle_request()

    httpd.server_close()


def start_server(timeout=TIMEOUT, port=PORT, forever=False):
    """ Starts the serve on a seperate thread with the given arguments, and returns the endpoint.

    Args:
        timeout (int, optional): Defaults to TIMEOUT=10 s.
        port (int, optional): Defaults to PORT=8000.
        forever (bool, optional): defaults to False.
    """
    server_thread = threading.Thread(target=_run_server, args=(timeout, port, forever))
    server_thread.start()
    return f'http://localhost:{port}'
