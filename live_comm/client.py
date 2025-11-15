import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
known_names = []


def listen_for_messages(client, chat_area):
    while True:
        try:
            message = client.recv(2048).decode()
            if message != "":
                username = message.split("~")[0]
                content = message.split("~")[1]
                chat_area.config(state="normal")
                chat_area.insert(tk.END, f"{username}: {content}\n")
                chat_area.yview(tk.END)
                chat_area.config()
            else:
                print("Message is empty ~")
        except:
            messagebox.showerror("Connection Error", "Disconnected from server.")
            break


def send_message_to_server(client, message_entry):
    """
    Sends the user's message to the server.
    """
    message = message_entry.get()
    if message.strip():
        try:
            client.sendall(message.encode("utf-8"))
            message_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")
    else:
        messagebox.showwarning("Warning", "Message cannot be empty.")


def communicate_to_server(client, chat_area, message_entry):
    global known_names
    username = simpledialog.askstring("Username", "Enter your username:")
    if username not in known_names:
        try:
            client.sendall(username.encode())
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to send username: {e}")
            return

        # Start a thread to listen for messages
        threading.Thread(target=listen_for_messages, args=(client, chat_area), daemon=True).start()
    elif username in known_names:
        messagebox.showerror("Invalid Username", "Username already exists.")
        return
    else:
        messagebox.showerror("Invalid Username", "Username cannot be empty.")
        exit(0)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(("127.0.0.1", 4000))
        print("Connected to server")
    except Exception as e:
        print(f"Failed to connect to the server: {e}")
        return

    window = tk.Tk()
    window.title("Chat Application")

    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state="disabled", height=20, width=50)
    chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    message_entry = tk.Entry(window, width=40)
    message_entry.grid(row=1, column=0, padx=10, pady=10)

    send_button = tk.Button(window, text="Send", width=10, command=lambda: send_message_to_server(client, message_entry))
    send_button.grid(row=1, column=1, padx=10, pady=10)

    communicate_to_server(client, chat_area, message_entry)

    def on_closing():
        try:
            client.close()
        except:
            pass
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()


if __name__ == "__main__":
    main()
