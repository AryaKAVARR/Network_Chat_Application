# Network_Chat_Application

### I have written client and server code for a simple chat application using sockets and threading in Python. This code allows multiple clients to connect to a server and send messages to each other. Below is an explanation of how the codes work:

#### :star:Server Code (server.py):
>1. The server creates a socket (server_socket) using socket.socket() and binds it to the local host and port 8546 using bind().
>2. It starts listening for incoming connections using listen(5), allowing up to 5 pending connections in the queue.
>3. The server enters a loop where it continuously waits for incoming client connections using accept(). When a new connection is accepted, a new thread is created to handle the client using threading.Thread, and the client's socket and address are passed to the handle_client function.
>4. The handle_client function runs in a separate thread for each client. It continuously receives messages from the client, broadcasts them to all other connected clients using the broadcast_message function, and removes the client if there's an error or if the client disconnects.
>5. The broadcast_message function sends the received message to all connected clients except the sender.

#### :star:Client Code (client.py):
>1. The client creates a socket (client_socket) and connects to the server running on the localhost and port 8546 using connect().
>2. It starts two separate threads: one for receiving messages (receive_thread) and another for sending messages (send_thread).
>3. The receive_messages function continuously receives messages from the server and prints them to the client's console.
>4. The send_messages function allows the client to input messages and sends them to the server.
>5. The server maintains a list of connected clients (clients) to keep track of all active connections.

### :fire:How to run?

To run the provided server and client code for simple chat application, follow these steps:

1. Save the Server and Client Code
>Save the server code in a Python file, for example, `server.py.`
>Save the client code in another Python file, for example, `client.py.`

2. Open Terminal (Command Prompt). 
>Open a terminal or command prompt on your computer. Make sure you have `Python` installed.

3. Run the Server. 
>In the terminal, navigate to the directory where you saved server.py. Then, run the server script by typing the following command:
```
python server.py 
```
OR
```
python3 server.py (if python3 installed)
```
OR
```
./server.py
```
>You should see a message indicating that the *server has started and is waiting for connections.*

4. Run the Clients. 
>Open additional terminals or command prompts for each client you want to run. In each client terminal, navigate to the directory where you saved `client.py.` Then, run the client script by typing the following command:
```
python client.py 
```
OR
```
python3 client.py (if python3 installed)
```
OR
```
./client.py
```
>Repeat this step for as many clients as you want to run. Each client will connect to the server.

5. Chatting
>You can now start sending messages between clients. Type a message in one client's terminal, press Enter, and you should see the message appearing in other clients' terminals through the server.

:fire:Remember that in this simple chat application, all clients connect to the same server on localhost. If you want to run clients on different machines or on the same machine but using different IP addresses or hostnames, you'll need to modify the server and client code accordingly.





