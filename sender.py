from socket import*
from pyDes import*
from DES import*
from RSA import*
from fileclient import*

text = readfile_plain()
key = readfile_key()
cipher = encodeAll(text,key)
writefile_cipher(cipher)
keytosend=encode_key()

serverName=input('enter the server name: ')
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(cipher.encode())
print("send a mail!")
clientSocket.close()

