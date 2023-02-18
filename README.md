# Overview

For this program I chose to do a client-server model. The providers of resource or service
are called servers. The service requesters are called the client. I made a python file for both the server and client. When I run the server, it will let me know it is running and listening for clients. When I run the client file, the GUI asks the client for their name, and waits for the server to respond on another GUI. Then, they are able to chat back and forth. 

As I wrote this program, I learned a great deal about UDP and TCP models. This shows the relationship in programs in application. The server component provides a function or service to many clients which initiates requests. 

[Software Demo Video](https://youtu.be/6K5T_w94bGQ)

# Network Communication

The client-server model allows clients and servers exchange messages in a request-response messaging pattern. I used TCP because it is realiable. Packets dropped in the network are and retransmitted by the sender. The data is read by the application in the order it was written by the sender. 

The format that I used to exchange messages is a graphical user interface also known as GUI.
# Development Environment

Python has libraries that I could import TCP socket functions. There are functions that allow the server to set up a "listening" socket. As we "listen", the next is to accept. Like I mentioned before, I made a GUI chat. The libraries that allowed me to do this is tkinter and it allowed me to modify the chat to my liking.
# Useful Websites

* [What's the difference between TCP and UDP?](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [Python Server Libraries](https://docs.python.org/3.6/library/socketserver.html)

# Future Work

* Redesign GUI
* Smoother start and set up