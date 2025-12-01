import socket
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()	
print('Listening on host & port : http://%s:%s'%(SERVER_HOST, SERVER_PORT))
print('Press ctrl+c to exit')

# Path file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:	
    client_connection, client_address = server_socket.accept() 
    #Request
    request = client_connection.recv(1024).decode() 
    print(request)

    response_line = 'HTTP/1.1 200 OK'.encode()
    entity_header = 'Content-Type: text/html'.encode()
    #Baca File HTML
    file = open(os.path.join(BASE_DIR, 'index.html'), 'r')
    body = file.read().encode()
    file.close()
    enter = '\r\n'.encode() 
    
    # Response
    response = b''.join([response_line, enter, entity_header, enter, enter, body])
    client_connection.send(response)
    client_connection.close() 
#End while
server_socket.close()
