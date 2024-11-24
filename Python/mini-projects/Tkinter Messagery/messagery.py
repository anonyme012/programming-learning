#############
# Libraries #
#############

import socket
import threading
import markdown as md
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from requests import get
from tkinterweb import HtmlFrame

############
# Fuctions #
############

### Complementary Windows ###

def open_settings_window() : 
    settings_window = tk.Toplevel(main_window)
    settings_window.geometry("300x300")
    settings_window.title("Settings")

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
    selector_setting_3_2.grid(row = 2, column = 2, sticky = "w")
    label_setting_4.grid(row = 3, column = 0, sticky = "w")
    selector_setting_4.grid(row = 3, column = 1, sticky = "w")
    label_setting_5.grid(row = 4, column = 0, sticky = "w")
    selector_setting_5.grid(row = 4, column = 1, sticky = "w")

    buttons_frame = tk.Frame(settings_window)
    buttons_frame.grid(row = 5, column = 0, columnspan = 3, pady = 10)
    launch_button = tk.Button(buttons_frame, text = "Launch Server", bg = "green", command = server_launching_sequence)
    launch_button.grid(row = 0, column = 0, pady = 10)
    connect_button = tk.Button(buttons_frame, text = "Connect", bg = "green", command = start_client)
    connect_button.grid(row = 0, column = 1, pady = 10)
    show_ip_button = tk.Button(buttons_frame, text = "Show IP", command = display_ip_address)
    show_ip_button.grid(row = 0, column = 2, pady = 10)
    quit_save_button = tk.Button(settings_window, text = "Close & Save", bg = "red", command = settings_window.destroy)
    quit_save_button.grid(row = 6, column = 0, columnspan = 3, pady = 10)

def open_documentation_window() : 
    documentation_text_var = """# Documentation
    """
    documentation_window = tk.Toplevel(main_window)
    documentation_window.geometry("300x300")
    documentation_window.title("Documentation")
    documentation_frame = HtmlFrame(documentation_window, messages_enabled = False)
    documentation_frame.load_html(md.markdown(documentation_text_var))
    documentation_frame.pack(fill = "both", expand = True)

##### Server #####

def start_server() : 
    try : 
        global server_socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", int(COMMUNICATION_PORT.get())))
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        tk.messagebox.showinfo("Successful", f"Server connected to {addr}")
        while True : 
            data = conn.recv(1024).decode()
            if not data : 
                break
            messages_text_module.insert("end", f"\n\nYour correspondant : \n{data}")
    except Exception as e : 
        tk.messagebox.showinfo("Server Error", "Unknown Server Error : \n\n" + str(e))

def server_launching_sequence() : 
    server_closing_sequence()
    try : 
        global server_thread
        server_thread = threading.Thread(target = start_server)
        server_thread.start()
    except Exception as e : 
        print(f"Error in server_launching_sequence : {e}")

def server_closing_sequence() : 
    try : 
        server_socket.close()
    except Exception as e : 
        print(f"Error in server_closing_sequence : {e}")
    try : 
        server_socket.shutdown(socket.SHUT_RDWR)
    except Exception as e : 
        print(f"Error in server_closing_sequence : {e}")
    try : 
        server_thread.join(2)
    except Exception as e : 
        print(f"Error in server_closing_sequence : {e}")

##### Client #####

def start_client() : 
    try : 
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((CORRESPONDANT_IP.get(), int(COMMUNICATION_PORT.get())))
    except Exception as e : 
        tk.messagebox.showerror("Client Error", "Impossible to connect to the server : \n\n" + str(e))

def client_closing_sequence() : 
    try : 
        client_socket.close()
    except Exception as e : 
        print(f"Error in client_closing_sequence : {e}")
    try : 
        client_socket.shutdown(socket.SHUT_RDWR)
    except Exception as e : 
        print(f"Error in client_closing_sequence : {e}")

##### General #####

def socket_closing_sequence() : 
    server_closing_sequence()
    client_closing_sequence()

def app_closing_sequence() : 
    # Closing Sockets
    try : 
        socket_closing_sequence()
    except Exception as e : 
        print(f"Error in app_closing_sequence : {e}")
    # Closing Windows
    try : 
        main_window.destroy()
    except Exception as e : 
        print(f"Error in app_closing_sequence : {e}")
    try : 
        settings_window.destroy()
    except Exception as e : 
        print(f"Error in app_closing_sequence : {e}")
    try : 
        documentation_window.destroy()
    except Exception as e : 
        print(f"Error in app_closing_sequence : {e}")

##### Special #####

def send_message() : 
    try : 
        content = message_textbox.get("1.0", "end").strip()
        message_textbox.delete("1.0", "end")
        client_socket.sendall(content.encode())
    except Exception as e : 
        tk.messagebox.showwarning("Message Not Sent", "Impossible to send the message : \n\n" + str(e))
    else : 
        messages_text_module.insert("end", f"\n\nMe : \n{content}")

def display_ip_address() : 
    try : 
        ipv4_response = get('https://api.ipify.org').text
        ipv6_response = get('https://api6.ipify.org').text
        tk.messagebox.showinfo("Show IP Address", "Your IPv4 address is : " + format(ipv4_response) + "\nYour IPv6 address is : " + format(ipv6_response))
    except Exception as e : 
        tk.messagebox.showerror("IP Address Error", "Impossible to get your IP address : \n\n" + str(e))

######################
# Launching Sequence #
######################

# Main widow creation
main_window = tk.Tk()
main_window.protocol("WM_DELETE_WINDOW", app_closing_sequence)

# Settings setting :-)
settings_window = tk.Toplevel(main_window)
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
settings_window.destroy()

#######
# GUI #
#######

# Window
main_window.geometry("600x600")
main_window.title("Python Messagery App")

# Top Toolbar
top_frame = tk.Frame(main_window, bd = 2, relief = tk.SOLID)
top_frame.pack(fill = "x", side = tk.TOP)
settings_button = tk.Button(top_frame, text = "Settings", command = open_settings_window)
settings_button.pack(side = tk.LEFT)
documentation_button = tk.Button(top_frame, text = "Documentation", command = open_documentation_window)
documentation_button.pack(side = tk.LEFT, expand = True)
quit_button = tk.Button(top_frame, text = "Quit", command = app_closing_sequence)
quit_button.pack(side = tk.RIGHT)

# Messages
messages_frame = tk.Frame(main_window, bd = 2, relief = tk.SOLID)
messages_text_module = tk.Text()

# Type & Send
message_composition_frame = tk.Frame(main_window, relief = tk.SOLID, bd = 2)
message_composition_frame.pack(fill = "x", side = tk.BOTTOM)
message_textbox = ScrolledText(message_composition_frame, wrap="word")
message_textbox.pack()
send_button = tk.Button(message_composition_frame, text = "Send", command = send_message)
send_button.pack()

############
# Mainloop #
############

main_window.mainloop()

###########################
# Todo List (by priority) #
###########################

# ++ Add messages time
# +  Fill the Documentation Page
#    Add more console logs & a GUI debugging mode
# -  Proper exit everywhere
# -  Add input verification
# -  Add AES-256 encryption support
# -  Add colors and formatting for a better understanding
# -  Add possibility to change the time format
# -- Add Markdown support
# -- Add the possiblity to send files
# -- Add the possiblity to use with roups of more than 2 people

########
# Bugs #
########

# - Settings variables are associated to the settings_window and not to the main_window : it can lead to edition and association errors