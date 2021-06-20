# Overview


By building this project I hoped to learn more about networking and how it can be accomplished in Python using a client server model.

This program contains both a server and a client that has a gui. The client can send messages to the server and the server can respond with a custom message. If the client sends "dog" or "cat" then an image will be served up respectively.

To start the programs cd to the directory holding these files and type `Python3 server.py` to start the server and then `Python3 client.py` to start the client.
PyQt5 needs to be installed. You can do this with `pip3 install pyqt5`

This software was purely for learning purposes

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/Nnio1nj1NNc)

# Network Communication


The architecture of this project is client/server and was accomplished by using python socketserver and socket.
It establishes a TCP connection from server to client and sends data as bytes over the socket stream.


# Development Environment

{Describe the tools that you used to develop the software}
Developed in Atom IDE
Written in Python 3
Libraries
 - socketserver
 - socket
 - pyqt5 for gui

Ubuntu vm running in Virtualbox for better understanding

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [socketserver documentation](https://docs.python.org/3/library/socketserver.html#module-socketserver)
* [QT documentation](https://doc.qt.io/qtforpython/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Scrolling message view in GUI
* Serve message to separate client
* Better GUI
