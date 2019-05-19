from socket import*
from RSA import*
from DES import*
from fileclient import*
from fileserver import*
import os,sys

serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket,addr=serverSocket.accept()
sentence=connectionSocket.recv(6666)
writefile_msg(sentence.decode())
mgs=readfile_msg()
key=decode_key()
mgs_1=decodeAll(mgs,key)
writefile_demsg(mgs_1)
writefile_demsg_key(key)
print("receive a mail!")
connectionSocket.close()
