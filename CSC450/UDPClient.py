from socket import *

# create clinet socket
client_socket = socket(AF_INET, SOCK_DGRAM)
print("Socket has been created")

server_ip = input("Server IP")
# set server port number
server_port = input("Server port: ")

# generate message to send
message = input("Message: ")

client_socket.sendto(message.encode(),(server_ip,int(server_port)))

recv_message, server_address = client_socket.recvfrom(2048)
print("Message: {}\nFrom : {}\n".format(recv_message.decode(), server_address))

client_socket.close()