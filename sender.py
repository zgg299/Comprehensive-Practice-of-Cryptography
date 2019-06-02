from socket import*
from pyDes import*
from DES import*
from RSA import*
from fileclient import*
from SHA1 import*
text = readfile_plain()
key = readfile_key()
cipher = encodeAll(text,key)
writefile_cipher(cipher)
keytosend=encode_key()
MAC=sha1()
serverName=input('enter the server name: ')
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(cipher.encode())
print("send the message already!")
clientSocket.send(keytosend.encode())
print("send the key already!")
sentence=clientSocket.recv(6666)
print(sentence.decode())
clientSocket.send(MAC.encode())
print("send the MAC already!")
clientSocket.close()

