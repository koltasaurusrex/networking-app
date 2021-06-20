import socket

from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 340, 700)
        self.title = "Python Networking"
        self.messageList = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.inputbox = QLineEdit(self)
        self.inputbox.move(20, 20)
        self.inputbox.resize(300,50)
        self.inputbox.setStyleSheet("background-color: black; color: white")


        self.label = QLabel(self)
        self.label.move(20, 120)
        self.label.resize(300,500)
        self.label.setText('Stuff is in this box')
        self.label.setStyleSheet("background-color: black; color: white")


        button=QPushButton('Send', self)
        button.move(100, 80)
        button.clicked.connect(self.connectToServer)
        self.show()

    def changeLabelText(self, text):
        self.label.setText(text)
    #
    # def addMessage(self, text):
    #     self.messageList.append(text)
    #     self.changeLabelText()

    def connectToServer(self, data):
        HOST, PORT = "192.168.0.3", 9999
        data = self.inputbox.text()
        received = ''
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        self.changeLabelText(received)


def main():

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
