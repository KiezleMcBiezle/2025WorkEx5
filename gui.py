import tkinter
from tkinter import font

#create window
window = tkinter.Tk()
window.geometry("350x500")
window.configure(bg="black")
window.title=("ReniChat")

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
chatdisplay = tkinter.Text(chatbox, bg="black", fg="orange", yscrollcommand=scrollbar, wrap="word", font=bold_font, state="disabled")
chatdisplay.pack(fill="both", expand=True)
scrollbar.config(comman=chatdisplay.yview)

#input field
entryframe= tkinter.Frame(window, bg="orange", padx=2, pady=2)
entryframe.pack(pady=10)

entry = tkinter.Entry(entryframe, bg="black", fg="orange", width=30)
entry.pack(side="left", padx=5)

#send button
def send_message(event=None):
    message = entry.get().strip()
    if message:
        chatdisplay.config(state="normal")
        chatdisplay.insert("end", f"Hubert: {message}\n")
        chatdisplay.config(state="disabled")
        chatdisplay.yview("end")  
        entry.delete(0, tkinter.END)

sendbutton = tkinter.Button(window, text="Send", command=send_message, bg="orange", fg="black")
sendbutton.pack(padx=20, pady=20)

#bind send button
entry.bind("<Return>", send_message)

#run
window.mainloop()