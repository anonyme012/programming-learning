#############
# Libraries #
#############

from socket import *
import tkinter as tk

############
# Fuctions #
############

def open_settings_window() : 
    print("")

def open_documentation_window() : 
    print("")

def quit_app() : 
    print("")

def configuration() : 
    global CORRESPONDANT_IP
    global TIME_DISPLAYING
    global MARKDOWN_SUPPORT
    global ENCRYPTION_PASSWORD
    CORRESPONDANT_IP = input("Your correspondant IP address (format : '255.255.255.255' or 'abcd:ef12:3456:7890:abcd:ef12:3456:7890') : ")
    TIME_DISPLAYING = input("Time format ('12' or '24') ('24' is default) : ")
    MARKDOWN_SUPPORT = input("Markdown support ('yes' or 'no') ('no' is default) : ")
    ENCRYPTION_PASSWORD = input("Encryption password (leave empty for no encryption) : ")
    # Add verification and optional port selection

def create_sockets(port) : 
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global server_socket
    server_socket.bind((get_local_ipv4_address(), port))
    server_socket.listen(5)

def connect_socket(host, port) : 
    client_socket.connect((host, port))

def close_connection() : 
    client_socket.shutdown()
    client_socket.close()
    server_socket.shutdown()
    server_socket.close()

def send_message(content) : 
    msg_length = len(content)
    total_sent = 0
    while total_sent < msg_length : 
        sent = client_socket.send(content[total_sent:])
        if sent == 0 : 
            raise RuntimeError("Socket connection broken.")
        total_sent = total_sent + sent

def get_local_ipv4_address() : 
    try : 
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s : 
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e : 
        return f"Error : {e}"

def receive_message() : 
    msg = client_socket.recv(1024)
    return msg

#######
# GUI #
#######

# Window
main_window = tk.Tk()
main_window.geometry("400x400")
main_window.title("Python Messagery App")

# Top Toolbar
top_frame = tk.Frame(main_window, bg = "#FFFFFF", bd = 2, relief = tk.SOLID)
top_frame.pack()
settings_button = tk.Button(top_frame, text = "Settings", command = "open_settings_window")
settings_button.grid(row = 0, column = 0)
docs_button = tk.Button(top_frame, text = "Documentation", command = "open_documentation_window")
docs_button.grid(row = 0, column = 1)
quit_button = tk.Button(top_frame, text = "Quit", command = "quit_app")
quit_button.grid(row = 0, column = 2)

# Messages
###

# Type & Send
###

############
# Mainloop #
############

main_window.mainloop()