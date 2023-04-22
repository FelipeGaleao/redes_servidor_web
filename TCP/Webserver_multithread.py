# Este servidor web suporta UM pedido de arquivo.
# Usar num navegador web "localhost:6789/index.html"

# O navegador vai pedir também "Favicon.ico". Criei uma exceção,
# Tem que rodar muito comportadamente para funcionar

# Completar o programa nos pontos indicados com   # /* XXXX */

# Import socket module
from socket import *
import sys  # In order to terminate the program
import threading


def handle_request(connectionSocket):
    try:
        # Receives the request message from the client
        # /* 4. PRIMITIVA RECEIVE DE SOCKETS */
        message = connectionSocket.recv(1024).decode()
        # print("Mensagem recebida: ", message)
        print("** Passou o ACCEPT **")

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        print("filename: ", filename)
        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character

        print("** Arquivo: ", filename)
        if filename == "/favicon.ico":
            return

        f = open(filename[1:])
        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()
        # Send the HTTP response header line to the connection socket
        # /* 5. PRIMITIVA SEND DE SOCKETS */
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close the client connection socket

        print("** Fecha Socket de conexão **")

        connectionSocket.close()

    except IOError:
        print("** IO Error **")

        # Send HTTP response header line for file not found (404)
        # /* 6. PRIMITIVA SEND DE SOCKETS */

        connectionSocket.send(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()
        )
        # Close the client connection socket
        # /* 7. PRIMITIVA CLOSE DE SOCKETS */
        connectionSocket.close()


# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Assign IP address to socket
# Bind the socket to server address and server port
# /* 1. PRIMITIVA BIND DE SOCKETS */
serverSocket.bind(("192.168.0.106", serverPort))


# Listen to at most 1 connection at a time
# /* 2. PRIMITIVA LISTEN DE SOCKETS */
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
    print("The server is ready to receive")

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()  # Establish the connection

    client_thread = threading.Thread(target=handle_request, args=(connectionSocket, addr))
    client_thread.start()

serverSocket.close()
sys.exit()
