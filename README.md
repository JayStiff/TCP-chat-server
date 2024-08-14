# TCP-chat-server
A basic multi-client chat server implemented in Python using sockets and threading. This project demonstrates the core concepts of networking and concurrent programming, allowing multiple clients to connect and communicate in real-time through a central server.
Features
Real-time communication between multiple clients
Broadcasting messages to all connected clients
Notifying when a client joins or leaves the chat
User-friendly interface for nickname selection
## Key Features
- Multi-Client Support:
The server can handle multiple clients simultaneously, allowing them to join the chat, send messages, and receive responses from other participants.
- Persistent Connections:
TCP ensures that a connection remains open as long as needed, providing a reliable stream of communication between the server and each client.
- Message Broadcasting:
The server receives messages from a client and broadcasts them to all other connected clients, ensuring everyone is part of the conversation.
- Threaded Client Handling:
Each client connection is managed in a separate thread, allowing the server to handle multiple clients concurrently without blocking the main execution thread.
- Connection Management:
The server can track connected clients, add new ones, and handle disconnections.
## How It Works
- Server Setup:
The server is initiated by creating a socket that listens for incoming connections on a specified IP address and port. Once a client connects, the server accepts the connection and spawns a new thread to handle communication with that client.
- Client Connection:
Clients connect to the server using a socket and then join the chat session. Each client runs in a separate thread on the server, ensuring that messages from one client do not block messages from another.
- Message Handling:
When a client sends a message, the server receives it and broadcasts the message to all other connected clients. This is done using a loop that iterates through all active connections.
Disconnection Handling:
If a client disconnects, the server detects the disconnection, closes the client's socket, and removes the client from the active list. This prevents the server from attempting to send messages to a disconnected client.
