# coding=utf-8
from socket import *
import re
import time
import json

try:
    file = open("./web.config.tocak", "rb")
    conf = json.loads(file.read())
    file.close()
except:
    print("Server run error: 'web.config.tocak not find")

def handle_client(client_socket):
    request = client_socket.recv(20480).decode("utf-8")
    request_header_lines = request.splitlines()

    try:
        print("Detailed log")

        for line in request_header_lines:
            print(line)
        print("Brief information")
        print("Access time ---->", time.asctime())
        print("Request way ---->", request_header_lines[0])
        print("file_path ---->", conf["http_config"]["index"] + re.match(r"[^/]+/([^\s]*)", request_header_lines[0]).group(1))

        ret = re.match(r"[^/]+/([^\s]*)", request_header_lines[0])
        if ret:
            file_path = conf["http_config"]["index"] + ret.group(1)
            retarray = [""]

            i = 0
            for word in ret.group(1):
                retarray.append(word)
                i = i + 1

            if len(retarray[len(ret.group(1))]) == 0:
                retarray[0] = "/"
            if retarray[len(ret.group(1))] == "/":
                file_path = conf["http_config"]["index"] + ret.group(1) + "index.html"
            if not(retarray[len(ret.group(1))] == "/") and not("index.html" in ret.group(1)):
                file_path = conf["http_config"]["index"] + ret.group(1) + "/index.html"

            print("file_path *******", file_path)

        print("log end=========================")
    except:
        print("=========================\nlog ERROR\n=========================")

    try:
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "\r\n"

        file_name = file_path

        file = open(file_name, "rb")
        response_body = file.read()
        file.close()

        client_socket.send(response_headers.encode("utf-8"))
        client_socket.send(response_body)
    except:
        response_headers = "HTTP/1.1 404 not found\r\n"
        response_headers += "\r\n"

        response_body = conf["error_page"]["404"]

        response = response_headers + response_body
        client_socket.send(response.encode("utf-8"))

    client_socket.close()

def main():
    try:
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_socket.bind(('', int(conf["http_config"]["port"])))
        server_socket.listen(128)

        print("Server run in 'ip:",conf["http_config"]["port"],"'")
        print("log on:")
    except:
        print("Server run error")
        exit()

    while True:
        client_socket, clientAddr = server_socket.accept()
        handle_client(client_socket)


if __name__ == "__main__":
    main()