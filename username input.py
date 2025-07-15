#import libraries
import tkinter
from tkinter import font
import socket
import threading

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

savebutton = tkinter.Button(window2, text="Save", command=save_username)
savebutton.pack()


#main -------------------------------
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

#input2 field
entryframe2= tkinter.Frame(window, bg="orange", padx=2, pady=2)
entryframe2.pack(pady=10)

entry2 = tkinter.Entry(entryframe2, bg="black", fg="orange", width=30)
entry2.pack(side="left", padx=5)

#send button
def send_message(event=None):
    message = entry.get().strip()
    if message:
        chatdisplay.config(state="normal")
        chatdisplay.insert("end", f"{username1}: {message}\n")
        chatdisplay.config(state="disabled")
        chatdisplay.yview("end")  
        entry.delete(0, tkinter.END)


sendbutton = tkinter.Button(window, text="Send", command=send_message, bg="orange", fg="black")
sendbutton.pack(padx=20, pady=20)

#send button 2
def send_message2(event=None):
    message = entry2.get().strip()
    if message:
        chatdisplay.config(state="normal")
        chatdisplay.insert("end", f"Amy: {message}\n")
        chatdisplay.config(state="disabled")
        chatdisplay.yview("end")  
        entry2.delete(0, tkinter.END)

sendbutton2 = tkinter.Button(window, text="Send", command=send_message2, bg="orange", fg="black")
sendbutton2.pack(padx=40, pady=40)

#bind send button
entry.bind("<Return>", send_message)
entry2.bind("<Return>", send_message2)
username.bind("<Return>", save_username)

#run
window.mainloop()