# coding=utf-8
from socket import *
import re
import time


def handle_client(client_socket):
    recv_data = client_socket.recv(2048).decode("utf-8")
    request_header_lines = recv_data.splitlines()
    print("Detailed log")
    for line in request_header_lines:
        print(line)

    print("Brief information")
    print("Access time ---->", time.asctime())
    print("Request way ---->", request_header_lines[0])
    print("file_path ---->", "./webapp/" + re.match(r"[^/]+/([^\s]*)", request_header_lines[0]).group(1))
    ret = re.match(r"[^/]+/([^\s]*)", request_header_lines[0])
    if ret:
        file_path = "./webapp/" + ret.group(1)
        retarray = [""]
        i = 0
        for word in ret.group(1):
            retarray.append(word)
            i = i + 1
        if len(retarray[len(ret.group(1))]) == 0:
            retarray[0] = "/"
        if retarray[len(ret.group(1))] == "/":
            file_path = "./webapp/"+ret.group(1)+"index.html"
        if not(retarray[len(ret.group(1))] == "/") and not("index.html" in ret.group(1)):
            file_path = "./webapp/" + ret.group(1) + "/index.html"
        print("file_path *******", file_path)
    print("log end=========================")

    try:
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "\r\n"
        file_name = file_path
        f = open(file_name, "rb")
        response_body = f.read()
        f.close()

        client_socket.send(response_headers.encode("utf-8"))
        client_socket.send(response_body)
    except:
        response_headers = "HTTP/1.1 404 not found\r\n"
        response_headers += "\r\n"
        response_body = "<title>404 error</title><h1>404 error</h1><hr><p>sorry,file not found.<br>Please check the URL you entered or contact developers.</p><p>tocak</p>"
        response = response_headers + response_body
        client_socket.send(response.encode("utf-8"))

    client_socket.close()


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 8888))
    server_socket.listen(128)
    print('Server run in "ip:7788"')
    print('log on:')
    while True:
        client_socket, clientAddr = server_socket.accept()
        handle_client(client_socket)


if __name__ == "__main__":
    main()