#发送方的文件操作
#将内容加密写入文件
def writefile_cipher(cipher):
    f=open("ciphermessages.txt",'w')
    f.write(cipher)
    f.close()
#读取明文
def readfile_plain():
    f=open("plainmessages.txt",'r')
    plain_message=f.read()
    return plain_message
#读取密钥
def readfile_key():
    f=open("DES_key_plain.txt",'r')
    key=f.read()
    f.close()
    return key 
#将密钥写入加密以后的密钥信息文件
def writefile_key(cipher):
    f=open("DES_key_cipher.txt",'w')
    f.write(cipher)
    f.close()

def write_p(cipher):
    f=open("p.txt",'w')
    f.write(cipher)
    f.close()

def write_q(cipher):
    f=open("q.txt",'w')
    f.write(cipher)
    f.close()

def write_e(cipher):
    f=open("e.txt",'w')
    f.write(cipher)
    f.close()

def write_n(cipher):
    f=open("n.txt",'w')
    f.write(cipher)
    f.close()