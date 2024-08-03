import threading
import socket

host = '127.0.0.1' # normal localhost
port = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))  # server is bound to the local host on port 77777
server.listen()

clients = [] #the list where we put all the new clients connecting to the server
nickname = [] # their nickname

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nickname[index]
            broadcast(f'{nickname} has left!'.encode('ascii'))
            nickname.remove(nickname)
            break

def recive():
    while True:
        client, address = server.accept()       #accepting clients
        print(f"Conneted with {str(address)}")

        client.send('NICK'.encode('ascii')) #sending clients the code word "NICK" so they can then send there nickname
        nickname = client.recv(1024).decode('ascii')
        nicknamez = []
        nicknamez.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!') #broadcasting to the server so everyone knows the nickname and that the client knows its recived
        broadcast(f'{nickname} has joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

recive()
