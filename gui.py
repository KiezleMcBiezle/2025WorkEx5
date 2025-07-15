import tkinter
from tkinter import font

#create window
window = tkinter.Tk()
window.geometry("250x250")
window.configure(bg="black")
window.title=("ReniChat")

#font
bold_font = font.Font(family="Handel Gothic", size=12, weight="bold")

#title at top of screen
label = tkinter.Label(window, text="ReniChat", bg="black", fg="orange", font=bold_font)
label.grid(row=0,column=5)

#input field
frame= tkinter.Frame(window, bg="orange", padx=2, pady=2)
frame.grid(row=100,column=0)

entry = tkinter.Entry(frame, bg="black", fg="orange")
entry.grid(row=100,column=0)

#chat display
chat_display = tkinter.Text(window, bg="black", fg="orange", wrap="word", font=bold_font, state="disabled")

#send button
def on_button_click():
    label = tkinter.Label(window, text="Sent!")
    label.grid(row=100,column=350)
    message = entry.get().strip()
    if message:
        chat_display.config(state="normal")
        chat_display.insert("end", f"Hubert: {message}\n")
        chat_display.config(state="disabled")
        chat_display.yview("end")  # Auto-scroll to the bottom
        entry.delete(0, tkinter.END)
    label = tkinter.Label(window, text=message,bg="black", fg="orange")
    label.grid(row=50,column=0)

button = tkinter.Button(window, text="Send", command=on_button_click, bg="orange", fg="black")
button.grid(row=100,column=300)


window.mainloop()