from socket import *
import sys

# create clinet socket
client_socket = socket(AF_INET, SOCK_STREAM)



# connect to server socket
client_socket.connect((sys.argv[1], int(sys.argv[2])))
print("HTTP request to server:")
print("{} /{} HTTP/1.1".format(sys.argv[3],sys.argv[4]))
print("Host: {}".format(sys.argv[1]))

if sys.argv[3] == "GET":
    # generate message to send
    message = ("{} {}".format(sys.argv[3], sys.argv[4]))
elif sys.argv[3] == "POST":
    print("Data: {}".format(sys.argv[5]))
    message = ("{} {} {}".format(sys.argv[3], sys.argv[4], sys.argv[5]))
else:
    message = ("{} {}".format(sys.argv[3], sys.argv[4]))


# send message to server
client_socket.send(message.encode())
print("HTTP response from server")

# receive message from server
received_message = client_socket.recv(2048)
print(" {}".format(received_message.decode()))

# close client socket
client_socket.close()




