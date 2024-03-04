import socket
import threading
from tkinter import *
from tkinter import simpledialog
import json

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Room")
        
        self.server_ip = simpledialog.askstring("Server IP", "Enter the server's IP:", parent=self.master)
        self.server_port = simpledialog.askinteger("Server Port", "Enter the server's port:", parent=self.master)
        self.username = simpledialog.askstring("Username", "Enter your username:", parent=self.master)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        
        self.client_socket.send(self.username.encode('utf-8'))
        
        self.setup_gui()
        
        threading.Thread(target=self.receive_message, daemon=True).start()

    def setup_gui(self):
        self.text_area = Text(self.master, state='disabled')
        self.text_area.pack(padx=20, pady=10)
        self.msg_entry = Entry(self.master)
        self.msg_entry.pack(padx=20, pady=10)
        self.msg_entry.bind("<Return>", self.send_message)
        self.send_button = Button(self.master, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)
        self.text_area.tag_configure('grey', foreground='grey', justify='center')

    def send_message(self, event=None):
        message = self.msg_entry.get()
        self.msg_entry.delete(0, END)
        if message.lower() == 'quit':
            self.client_socket.send('quit'.encode('utf-8'))
            self.client_socket.close()
            self.master.quit()
        else:
            self.client_socket.send(message.encode('utf-8'))

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message == '':
                    break
                self.display_message(message)
            except Exception as e:
                print("Connection to server lost:", e)
                break

    def display_message(self, message):
        self.text_area.config(state='normal')
        if "has joined the chat!" in message or "You're currently alone in this room." in message or "has left the chat." in message:
            self.text_area.insert(END, message + "\n", 'grey')
        else:
            self.text_area.insert(END, message + "\n")
        self.text_area.config(state='disabled')
        self.text_area.yview(END)

root = Tk()
app = ChatClient(root)
root.mainloop()