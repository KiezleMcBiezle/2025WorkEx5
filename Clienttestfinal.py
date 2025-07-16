#import libraries
import tkinter
from tkinter import font
import socket
from threading import Thread
from datetime import datetime
import os
from tkinter import filedialog

#main -------------------------------
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 1234

#initialise TCP socket
s = socket.socket()
#Connect to the server
s.connect((SERVER_HOST, SERVER_PORT))


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

    def send_message():
        message = entry.get().strip()
        if message:
            date_now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            chatdisplay.config(state="normal")
            chatdisplay.config(state="disabled")
            chatdisplay.yview("end")  
            entry.delete(0, tkinter.END)

            to_send = f"[{date_now}] {username1}: {message}"
            s.sendall(to_send.encode())

    def listen_for_messages():
        while True:
            # use try-except to handle any errors that may happen with .recv()
            try:
                to_recieve = s.recv(1024).decode()

                def update_chat():
                    chatdisplay.config(state="normal")
                    chatdisplay.insert("end", f"{to_recieve}\n")
                    chatdisplay.config(state="disabled")
                    chatdisplay.yview("end") 
                
                # need to use window.after as we need to update the GUI outside of the deamon thread
                # in the main thread where mainloop runs
                window.after(0, update_chat)
            except Exception as e:
                print(f"Error recieved message: {e}")
                break

    t = Thread(target=listen_for_messages, daemon=True)
    t.start()

    sendbutton = tkinter.Button(buttonframe, text="Send", command=send_message, bg="orange", fg="black")
    sendbutton.pack(side="left", padx=10)

    #bind send button
    entry.bind("<Return>", send_message)


    #run
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
    window2.destroy()
    openchat()

savebutton = tkinter.Button(window2, text="Save", command=save_username)
savebutton.pack()
username.bind("<Return>", save_username)
window2.mainloop()