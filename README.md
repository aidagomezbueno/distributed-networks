# Python Chat Application

## Overview

This Python Chat Application provides a platform for real-time text-based communication between multiple clients through a central server. It's designed with simplicity and functionality in mind, allowing users to easily chat in a shared room.

## Functionality

- **Multi-Client Communication**: Supports multiple clients simultaneously, enabling group discussions in a single chat room.
- **Server-Client Architecture**: Utilizes a server to manage connections, relay messages, and handle clients joining and leaving.
- **Real-time Interaction**: Delivers messages instantly, ensuring dynamic and engaging conversations.
- **GUI Client**: Offers a graphical user interface for client interactions, making the chat accessible and easy to use.
- **Username Customization**: Allows users to set a unique username upon joining, providing identity within the chat room.

## Implementation

The application is implemented in Python, using the following key components:

- **Sockets**: Facilitate network communication between the server and clients, enabling message passing and connection management.
- **Threading**: Ensures concurrent handling of multiple clients by the server, as well as seamless UI updates and network communication on the client side.
- **Tkinter**: Used to build the client's graphical user interface, providing input fields for messages, a display area for the chat, and buttons for actions like sending messages.

## How to Run

### Setting Up the Server

1. Navigate to the project directory in your terminal.
2. Run the server with the following command:
   ```
   python server.py
   ```
   This will start the server and wait for client connections.

### Stopping the Server

- To stop the server, press `Ctrl + C` in the terminal where the server is running. This command sends an interrupt signal to the server process, allowing it to terminate gracefully and close any existing client connections properly.

### Connecting Clients

1. Open a new terminal window for each client.
2. Navigate to the project directory.
3. Run the client with the following command:
   ```
   python client.py
   ```
4. Upon startup, each client will be prompted to enter the server's IP address, the port number, and a username.

- To properly connect with the server:
  - IP address: '127.0.0.1'
  - Port number = 12345

### Chatting

- Once connected, users can type messages into the input field and press the "Send" button or the Enter key to broadcast their message to all connected clients.

### Exiting the Chat

- Users can exit the chat by typing "quit" in the message input field or closing the chat window.

---

**Note:** Replace `python` with `python3` in the commands above if your system requires it to invoke Python 3.
