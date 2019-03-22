#Michael Gonzalez
#!/usr/bin/python
from socket import*

serverName = raw_input("Enter your desired server Address (localhost or 127.0.0.1): ")
serverPort = int(input("Enter your desired server Port: "))
serverAddress = (serverName,serverPort)

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(serverAddress)
command = raw_input("Enter your command: L/l for lowercase. U/u for uppercase. C/c for camelcase.")
command = command.upper()
if (command == 'L'):
    message = raw_input("Enter your message:")
    command = command+ " " +message
    clientSocket.send(command.encode())
elif (command == 'U'):
    message = raw_input("Enter your message:")
    command = command+ " " +message
    clientSocket.send(command.encode())
elif (command == 'C'):
    message = raw_input("Enter your message:")
    command = command+ " " +message
    clientSocket.send(command.encode())
modMessage = clientSocket.recv(2048)

print ("From server :",serverName, modMessage)
