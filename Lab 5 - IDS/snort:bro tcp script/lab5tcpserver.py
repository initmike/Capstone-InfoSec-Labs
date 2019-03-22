#Michael Gonzalez
#!/usr/bin/python
from socket import*

serverPort = int(input("Enter your desired Port number or enter 0 for default port of 9999:"))
if (serverPort == 0):
        serverPort = int(9999)       
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print ("The server is ready to receive.")

while True:
        connectionSocket, clientAddr = serverSocket.accept()
        message = connectionSocket.recv(2048)
        list1 = message.split(None,1)
        command = list1[0]
        msg2 = list1[1]
        print ("received from: ", msg2, clientAddr[0], clientAddr[1])
        if (command == "U"):
                capMessage = msg2.upper()
                connectionSocket.send(capMessage.encode())
        elif (command == "L"):
                lowmessage = msg2.lower()
                connectionSocket.send(lowmessage.encode())
        elif (command == "C"):
                cammessage = msg2.title()
                connectionSocket.send(cammessage.encode())
        connectionSocket.close()
        
