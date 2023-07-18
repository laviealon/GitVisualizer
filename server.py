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


if __name__ == '__main__':
    Handler = CustomHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at ", f"http://localhost:{PORT}/")

    start_time = time.time()
    while time.time() - start_time < TIMEOUT:
        httpd.handle_request()

    httpd.server_close()

