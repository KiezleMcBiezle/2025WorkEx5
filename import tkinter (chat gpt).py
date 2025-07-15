import tkinter as tk
from tkinter import font

# Create window
window = tk.Tk()
window.geometry("350x500")
window.configure(bg="black")
window.title("ReniChat")

#login pop up
def show_login_popup():
    popup = tk.Toplevel()
    popup.title("Login")
    popup.geometry("300x120")
    popup.configure(bg="black")
    popup.grab_set()

    tk.Label(popup, text="Enter your name:", bg="black", fg="orange").pack(pady=5)
    name_entry = tk.Entry(popup, bg="white", fg="black")
    name_entry.pack()


# Font
bold_font = font.Font(family="Handel Gothic", size=14, weight="bold")

# Title label
title_label = tk.Label(window, text="ReniChat", bg="black", fg="orange", font=bold_font)
title_label.pack(pady=10)

# Frame for messages and scrollbar
messages_frame = tk.Frame(window, bg="black")
messages_frame.pack(fill="both", expand=True, padx=10)

# Add scrollbar
scrollbar = tk.Scrollbar(messages_frame)
scrollbar.pack(side="right", fill="y")

# Text widget for message display
chat_display = tk.Text(messages_frame, bg="black", fg="white", yscrollcommand=scrollbar.set, wrap="word", state="disabled")
chat_display.pack(fill="both", expand=True)
scrollbar.config(command=chat_display.yview)

# Entry and send button frame
entry_frame = tk.Frame(window, bg="orange", padx=2, pady=2)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, bg="black", fg="orange", width=30)
entry.pack(side="left", padx=5)

# Function to send messages
def send_message(event=None):
    message = entry.get().strip()
    if message:
        chat_display.config(state="normal")
        chat_display.insert("end", f"Hubert: {message}\n")
        chat_display.config(state="disabled")
        chat_display.yview("end")  # Auto-scroll to the bottom
        entry.delete(0, tk.END)

# Button
send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="orange", fg="black")
send_button.pack(side="left")

# Bind Enter key to send
entry.bind("<Return>", send_message)

# Start GUI
show_login_popup()
window.mainloop()
