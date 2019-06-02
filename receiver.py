from socket import*
from RSA import*
from DES import*
from fileclient import*
from fileserver import*
from SHA1 import*
import os,sys

serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket,addr=serverSocket.accept()
sentence=connectionSocket.recv(6666)
print('receive the message!')
writefile_msg(sentence.decode())
sentence1=connectionSocket.recv(6666)
print('receive the key!')
writefile_msg_key(sentence1.decode())
mgs=readfile_msg()
key=decode_key()
mgs_1=decodeAll(mgs,key)
writefile_demsg(mgs_1)
writefile_demsg_key(key)                                                                                                                                                                                        
reply="please send the MAC!"
connectionSocket.send(reply.encode())
MAC_rec=connectionSocket.recv(6666).decode()
print("receive the MAC!")
connectionSocket.close()

MAC_self=sha1()
print('the MAC is'+MAC_self)
print('the MAC receive is'+MAC_rec)
if MAC_rec==MAC_self:
    print("it is right!")
else:
    print("message is wrong!")
