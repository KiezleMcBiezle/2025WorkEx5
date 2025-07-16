import socket
import random
from threading import Thread
from datetime import datetime

# SERVER_HOST = "192.168.55.19"
# SERVER_PORT = 1234 
# separator_token = "<SEP>" 

# s = socket.socket()
# s.connect((SERVER_HOST, SERVER_PORT))

# username = ""

# def listen_for_messages():
#     while True:
#         message = s.recv(1024).decode()
#         recieve_message(message)
#         print("\n" + message)

# t = Thread(target=listen_for_messages)
# t.daemon = True
# t.start()

# while True:
#     to_send =  input()
#     if to_send.lower() == 'q':
#         break
#     date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
#     to_send = f"[{date_now}] {username}{separator_token}{to_send}"
#     s.sendall(to_send.encode())
# s.close()

import tkinter
from tkinter import font
import socket
import threading

#main -------------------------------
def openchat():
    #create window
    window = tkinter.Tk()
    window.geometry("350x500")
    window.configure(bg="black")
    window.title("ReniChat")

    #font
    bold_font = font.Font(family="Handel Gothic", size=12, weight="bold")

    #title at top of screen
    titlelabel = tkinter.Label(window, text="ReniChat", bg="black", fg="orange", font=bold_font)
    titlelabel.pack(pady=10)

    #chatbox
    chatbox = tkinter.Frame(window, bg="black")
    chatbox.pack(fill="both", expand=True, padx=10)

    #scrollbar
    scrollbar = tkinter.Scrollbar(chatbox)
    scrollbar.pack(side="right", fill="y")

    #chat display
    chatdisplay = tkinter.Text(chatbox, bg="black", fg="orange", yscrollcommand=scrollbar.set, wrap="word", font=bold_font, state="disabled")
    chatdisplay.pack(fill="both", expand=True)
    scrollbar.config(command=chatdisplay.yview)

    #input field
    entryframe= tkinter.Frame(window, bg="orange", padx=2, pady=2)
    entryframe.pack(pady=10)

    entry = tkinter.Entry(entryframe, bg="black", fg="orange", width=30)
    entry.pack(side="left", padx=5)


    #send button
    buttonframe = tkinter.Frame(window, bg="black")
    buttonframe.pack(padx=5, pady=20)

    def display_message(event = None):
        message = entry.get().strip()
        if message:
            chatdisplay.config(state="normal")
            chatdisplay.insert("end", f"{username1}: {message}\n")
            chatdisplay.config(state="disabled")
            chatdisplay.yview("end")  
            entry.delete(0, tkinter.END)

    def recieve_message(message, event = None):
        chatdisplay.config(state="normal")
        chatdisplay.insert("end", f"{username1}: {message}\n")
        chatdisplay.config(state="disabled")
        chatdisplay.yview("end")  
        entry.delete(0, tkinter.END) 

    sendbutton = tkinter.Button(buttonframe, text="Send", command=display_message, bg="orange", fg="black")
    sendbutton.pack(side="left", padx=10)

    #bind send button
    entry.bind("<Return>", display_message)

    SERVER_HOST = "192.168.55.19"
    SERVER_PORT = 1234 
    separator_token = "<SEP>" 

    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))

    username = ""

    def listen_for_messages():
        while True:
            message = s.recv(1024).decode()
            recieve_message(message)
            print("\n" + message)

    listen = Thread(target=listen_for_messages)
    listen.daemon = True
    listen.start()

    def send_messages():
        to_send =  input()
        if to_send.lower() == 'q':
            return
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        to_send = f"[{date_now}] {username}{separator_token}{to_send}"
        display_message()
        s.sendall(to_send.encode())

    send = Thread(target=send_messages)
    send.daemon = True
    send.start()    
    s.close()
    window.mainloop()

#input username window ------------------------
username1=""

window2 = tkinter.Tk()
#title
window2.title("Username")
#heading
window2label = tkinter.Label(window2, text="Enter your username: ")
window2label.pack()
#input field
username = tkinter.Entry(window2)
username.pack()

#button
def save_username(event=None):
    global username1
    username1 = username.get()
    username = username1
    window2.destroy()
    openchat()
 
savebutton = tkinter.Button(window2, text="Save", command=save_username)
savebutton.pack()
username.bind("<Return>", save_username)
window2.mainloop()

