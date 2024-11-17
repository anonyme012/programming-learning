#############
# Libraries #
#############

from socket import *
import tkinter as tk
import threading
import markdown as md
from tkinterweb import HtmlFrame

############
# Fuctions #
############

### Complementary Windows ###

def open_settings_window() : 
    settings_window = tk.Tk()
    settings_window.geometry("300x300")
    settings_window.title("Settings")

    global CORRESPONDANT_IP
    global COMMUNICATION_PORT
    global TIME_FORMAT
    global MARKDOWN_SUPPORT
    global ENCRYPTION_PASSWORD
    CORRESPONDANT_IP = tk.StringVar(master = settings_window, value = "")
    COMMUNICATION_PORT = tk.StringVar(master = settings_window, value = "9250")
    TIME_FORMAT = tk.IntVar(master = settings_window, value=24)
    MARKDOWN_SUPPORT = tk.BooleanVar(master = settings_window, value = False)
    ENCRYPTION_PASSWORD = tk.StringVar(master = settings_window, value = "")

    label_setting_1 = tk.Label(settings_window, text = "Correspondant IP Address (IPv4 or IPv6) : ")
    selector_setting_1 = tk.Entry(settings_window, textvariable = CORRESPONDANT_IP)

    label_setting_2 = tk.Label(settings_window, text = "Communication Port (from 1 to 65535) : ")
    selector_setting_2 = tk.Entry(settings_window, textvariable = COMMUNICATION_PORT)

    label_setting_3 = tk.Label(settings_window, text = "Time Format : ")
    selector_setting_3_1 = tk.Radiobutton(settings_window, text = "12", variable = TIME_FORMAT, value = 12)
    selector_setting_3_2 = tk.Radiobutton(settings_window, text = "24", variable = TIME_FORMAT, value = 24)

    label_setting_4 = tk.Label(settings_window, text = "Markdown Support : ")
    selector_setting_4 = tk.Checkbutton(settings_window, variable = MARKDOWN_SUPPORT)

    label_setting_5 = tk.Label(settings_window, text = "Encryption Password (leave empty for no encryption) : ")
    selector_setting_5 = tk.Entry(settings_window, textvariable = ENCRYPTION_PASSWORD, show = "*")

    label_setting_1.grid(row = 0, column = 0, sticky = "w")
    selector_setting_1.grid(row = 0, column = 1, sticky = "w")
    label_setting_2.grid(row = 1, column = 0, sticky = "w")
    selector_setting_2.grid(row = 1, column = 1, sticky = "w")
    label_setting_3.grid(row = 2, column = 0, sticky = "w")
    selector_setting_3_1.grid(row = 2, column = 1, sticky = "w")
    selector_setting_3_2.grid(row = 2, column = 1, sticky = "w")
    label_setting_4.grid(row = 3, column = 0, sticky = "w")
    selector_setting_4.grid(row = 3, column = 1, sticky = "w")
    label_setting_5.grid(row = 4, column = 0, sticky = "w")
    selector_setting_5.grid(row = 4, column = 1, sticky = "w")

    quit_save_button = tk.Button(settings_window, text = "Close & Save", command = settings_window.destroy)
    quit_save_button.grid(row = 5, column = 0, columnspan = 2, pady = 10)

    settings_window.mainloop()
    # Add verification
    # VARIABLE.get()

def open_documentation_window() : 
    documentation_text_var = """# Documentation
    """
    documentation_window = tk.Tk()
    documentation_window.geometry("300x300")
    documentation_window.title("Documentation")
    documentation_frame = HtmlFrame(documentation_window, messages_enabled = False)
    documentation_frame.load_html(md.markdown(documentation_text_var))
    documentation_frame.pack(fill="both", expand=True)
    documentation_window.mainloop()

### Socket Functions ###

def create_sockets() : 
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_sockets() : 
    client_socket.connect((CORRESPONDANT_IP, COMMUNICATION_PORT))
    server_socket.bind((get_local_ipv4_address(), COMMUNICATION_PORT))
    server_socket.listen(5)

def close_connection() : 
    client_socket.shutdown()
    client_socket.close()
    server_socket.shutdown()
    server_socket.close()

def send_message() : 
    content = message_textbox.get("1.0", "end").strip()
    message_textbox.delete("1.0", "end")
    ###
    msg_length = len(content)
    total_sent = 0
    while total_sent < msg_length : 
        sent = client_socket.send(content[total_sent:])
        if sent == 0 : 
            raise RuntimeError("Socket connection broken.")
        total_sent += sent

def get_local_ipv4_address() : 
    try : 
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s : 
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e : 
        return f"Error : {e}"

def receive_message() : 
    while True : 
        msg = client_socket.recv(1024)
        return msg

######################
# Launching Sequence #
######################

create_sockets()
connect_sockets()

listening_thread = threading.Thread(target = receive_message)
listening_thread.start()

#######
# GUI #
#######

# Window
main_window = tk.Tk()
main_window.geometry("600x600")
main_window.title("Python Messagery App")

# Top Toolbar
top_frame = tk.Frame(main_window, bd = 2, relief = tk.SOLID) # Add BG and take all the space
top_frame.pack(fill = "x", side = tk.TOP)
settings_button = tk.Button(top_frame, text = "Settings", command = open_settings_window)
settings_button.pack(side = tk.LEFT)
documentation_button = tk.Button(top_frame, text = "Documentation", command = open_documentation_window)
documentation_button.pack(side = tk.LEFT, expand = True)
quit_button = tk.Button(top_frame, text = "Quit", command = main_window.destroy)
quit_button.pack(side = tk.RIGHT)

# Messages
###

# Type & Send
message_composition_frame = tk.Frame(main_window, relief = tk.SOLID, bd = 2) # BG
message_composition_frame.pack(fill = "x", side = tk.BOTTOM)
message_textbox = tk.Text(message_composition_frame, bd = 1)
message_textbox.pack()
send_button = tk.Button(message_composition_frame, text = "Send", command = send_message)
send_button.pack()

############
# Mainloop #
############

main_window.mainloop()

close_connection()

#############
# Todo List #
#############

# ++ The messages box displaying interface
# +  Error Management in every function + global
# +  Fill the Documentation Page
#    Add character encoding for special chars
# -  Add input verification
# -  Add encryption
# -- Add Markdown support

########
# Bugs #
########

# Bad settings VARIABLES types used in fuctions
# The `recieve_message()` function stops after one reception because of the `return` statement