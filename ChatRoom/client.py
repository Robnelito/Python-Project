import socket
from threading import Thread
import tkinter

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("ChatRoom")
top.iconbitmap("icone/logo.ico")
top.geometry("360x540")
top.resizable(width=False, height=False)
top['bg'] = '#3dc66d'

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
# my_msg.create_oval(1,1,30,60, fill='#3dc66d', outline=root.cget("bg"))
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=30, width=60, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

photo = tkinter.PhotoImage(file='icone/request.png')
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.place(x='100', y='503')
send_button = tkinter.Button(top, image=photo, bg='#fff',command=send)
# send_button.create_oval(1, 1, 30, 30, fill="#3dc66d", outline=root.cget("bg"))
send_button.place(x='240', y='500')

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = '192.168.43.142'
PORT = 8080
# HOST = input('Enter host: ')
# PORT = input('Enter port: ')
# if not PORT:
#     PORT = 8080
# else:
#     PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()