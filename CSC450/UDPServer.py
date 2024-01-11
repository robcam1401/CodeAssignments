from socket import*

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('',12000))
print("Server is ready to recieve messages...\n")

while(True):
    message, client_address = server_socket.recvfrom(2048)
    print("Message: {}\nFrom: {}\n".format(message.decode()))

    modified_message = message.upper()
    print("Modified message: {}\n".format(modified_message.decode()))

    server_socket.sentto(modified_message, client_address)
    print("message sent...")
