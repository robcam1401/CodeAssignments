from socket import *
import os.path

# create server socket
server_socket = socket(AF_INET, SOCK_STREAM)
# bind socket to port number
server_socket.bind(('', 12000))
# keep socket listening to connections
server_socket.listen(1)
print("Server is ready to connect...\n")


# run forever loop to connect and receive messages
while(True):
    # create connection socket
    connection_socket, address = server_socket.accept()    
    print("Connection established with.{}\n".format(address))

    # receive message from connection socket
    incoming_message = connection_socket.recv(2048)
    

    modified_message = incoming_message.decode().split()
    #print("Modified message: {} {}\n".format(modified_message[0].decode(),modified_message[1].decode()))
    print(modified_message)

    if modified_message[0] == "GET":
        if os.path.exists(modified_message[1]):
            file=open(modified_message[1])
            f = (file.read())
            new_message = "HTTP/1.1 200 OK\n {}".format(f) 
        else:
            new_message = "HTTP/1.1 404 Not Found"
    elif modified_message[0] == "POST":
        if os.path.exists(modified_message[1]):
            message =' '.join(modified_message[2:])
            file=open(modified_message[1],"a")
            file.write(message)
            file.close()
            f=open(modified_message[1])
            f_read=f.read()

            print(message)
            new_message = "HTTP/1.1 201 Created\n {}".format(f_read)
        else:
            new_message = "HTTP/1.1 400 Bad Request"
    else:
        if os.path.exists(modified_message[1]):
            message =""
            file=open(modified_message[1],"w")
            file.write(message)
            file.close()
            f=open(modified_message[1])
            f_read=f.read()

            print(message)
            new_message = "HTTP/1.1 204 no Content\n {}".format(f_read)
        else:
            new_message = "HTTP/1.1 404 Not Found"
    
    connection_socket.send(new_message.encode())
    print("Message sent\n")


    # # close connection socket
    connection_socket.close()
