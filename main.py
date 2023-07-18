import webbrowser
import server


def open_webpage(url):
    webbrowser.open(url)


if __name__ == '__main__':
    endpoint = server.start_server()
    open_webpage(endpoint)

