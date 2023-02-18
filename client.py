import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = "localhost"
PORT = 9090

class Client:
    def __init__(self, host, port):
        # Client Socket and connection
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        # Draw gui
        message = tkinter.Tk()
        message.withdraw()

        # Get nickname from the user
        self.nickname = simpledialog.askstring("Nickname", "Please choose nickname", parent=message)

        # Gui not yet build
        self.gui_done = False

        # Connection running
        self.running = True
        
        # Build thread for gui and connect to server
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)
        gui_thread.start()
        receive_thread.start()

    # Build the gui
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="navy")

        self.chat_label = tkinter.Label(self.win, text="Chat", bg="lightgray")
        self.chat_label.config(font=("Consolas", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.message_label = tkinter.Label(self.win, text="Chat", bg="lightgray")
        self.message_label.config(font=("Consolas", 12))
        self.message_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Consolas", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.win.protocol("WM_DELETE_Window", self.stop)
        self.win.mainloop()

    
    def write(self):
        # Get the text from message box and send to server and close
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode("utf-8"))
        self.input_area.delete('1.0', 'end')
    

    def stop(self):
        # Close the program
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)
        

    # Handling the connection from Server
    def receive(self):
        while self.running:
            try:
                # Decod the messages sent
                message = self.sock.recv(1024).decode("utf-8")
                if message == "NICK":
                    self.sock.send(self.nickname.encode("utf-8"))
                else:
                    # Append the message at the end
                    if self.gui_done:
                        self.text_area.config(state="normal")
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')

            except ConnectionAbortedError:
                break
            except:
                print("Error, sorry")
                self.sock.close()
                break

client = Client(HOST, PORT)




