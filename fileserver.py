#接收方的文件操作
#将接收到的信息存入文件
def writefile_msg(cipher):
    f=open("recmessages.txt",'w')
    f.write(cipher)
    f.close()
#读取接收到的内容文件
def readfile_msg():
    f=open("recmessages.txt",'r')
    msg=f.read()
    f.close()
    return msg
#将接收到的密钥存入文件
def writefile_msg_key(cipher):
    f=open("DES_key_rec.txt",'w')
    f.write(cipher)
    f.close()
#读取接收到的密钥文件
def readfile_msg_key():
    f=open("DES_key_rec.txt",'r')
    msg=f.read()
    f.close()
    return msg
#将解密信息写入解密信息文件
def writefile_demsg(cipher):
    f=open("decryptionmessages.txt",'w')
    f.write(cipher)
    f.close()
#将解密密钥写入密钥信息文件
def writefile_demsg_key(cipher):
    f=open("DES_key_decryption.txt",'w')
    f.write(cipher)
    f.close()

def read_p():
    f=open("p.txt",'r')
    msg=f.read()
    f.close()
    return msg

def read_q():
    f=open("q.txt",'r')
    msg=f.read()
    f.close()
    return msg

def read_e():
    f=open("e.txt",'r')
    msg=f.read()
    f.close()
    return msg

def read_n():
    f=open("n.txt",'r')
    msg=f.read()
    f.close()
    return msg

