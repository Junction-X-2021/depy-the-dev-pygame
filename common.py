import socket

current_stage = 1
selected_index = 0

server_address = "ec2-52-79-251-108.ap-northeast-2.compute.amazonaws.com"
server_port = 8080
server_socket: socket.socket
