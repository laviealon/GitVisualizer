import webbrowser
import server


def open_webpage():
    endpoint = server.start_server(port=4000)
    webbrowser.open_new_tab(endpoint)


if __name__ == '__main__':
    open_webpage()
