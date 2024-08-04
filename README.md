# TCP-chat-server
A basic multi-client chat server implemented in Python using sockets and threading. This project demonstrates the core concepts of networking and concurrent programming, allowing multiple clients to connect and communicate in real-time through a central server.
Features
Real-time communication between multiple clients
Broadcasting messages to all connected clients
Notifying when a client joins or leaves the chat
User-friendly interface for nickname selection
Prerequisites
Python 3.x
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/multi-client-chat-server.git
Navigate to the project directory:

bash
Copy code
cd multi-client-chat-server
Usage
Start the Server:

Open a terminal and run the following command to start the server:

bash
Copy code
python server.py
Connect a Client:

Open another terminal and run the following command to start a client:

bash
Copy code
python client.py
Enter a nickname when prompted.

Communicate:

Type messages in the client terminal and press Enter to send them.
All connected clients will receive the messages in real-time.
