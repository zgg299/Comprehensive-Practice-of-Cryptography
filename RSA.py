llen = 512 
import random
import time
from DES import*
from fileclient import*
from fileserver import*
def qp(a,x,mod = 1e9+7):
    ans = 1; a %= mod
    while x:
        if x&1:
            ans = a*ans%mod
        a = a*a%mod
        x >>= 1
    return ans
def gcd(a,b):
    if b == 0 : return a
    return gcd(b,a%b)

def egcd(a,b,x,y): #return ans,x,y
    if b == 0: return 1,0
    x,y = egcd(b,a%b,x,y)
    temp = x
    x = y
    y = temp - a//b*y#// stand 整除
    return x,y

def inverse(a,mod):
    x,y = 1,1
    x,y = egcd(a,mod,x,y)
    return ( x%mod + mod ) % mod

def mltest(n,times = 50):
    if(n == 2): return True
    if(n < 2 or not(n&1)): return False
    temp = 0
    u = n-1
    while (u&1) == 0 : 
        temp+=1
        u >>= 1
    for i in range(times):
        a = random.randint(1,n-1)
        x = qp(a,u,n)
        for j in range(temp):
            y = x * x % n
            if y==1 and x!=1 and x!=n-1: return False
            x = y
        if x != 1 : return False
    return True

def gprime():
    p = 0
    while not p:
        temp = random.randint(1,(1<<llen)-1)
        if mltest(temp) : p = temp
    return p


def encode_key():
    msg=readfile_key()
    text =hexStringToDec(msg) 
    p,q = gprime(),gprime()
    while(p == q): q = gprime() 
    n = p*q; 
    fn = (p-1)*(q-1)
    e = 0
    while 1:
        e = random.randint(2,fn-1)
        if gcd(e,fn) == 1 : break    
    cipher = qp(text,e,n)
    writefile_key(str(cipher))#存入的为十进制
    write_p(str(p))
    write_q(str(q))
    write_e(str(e))
    write_n(str(n))
    return str(cipher)

def decode_key():
    tempmsg=readfile_msg_key()
    cipher=int(tempmsg)
    e=int(read_e())
    n=int(read_n())
    p=int(read_p())
    q=int(read_q())
    fn=(p-1)*(q-1)
    pkey = inverse(e,fn)
    msg=qp(cipher,pkey,n)
    writefile_demsg_key(DecTohexString(msg))
    return DecTohexString(msg)
def hexStringToDec(str):
    return int(str,16)

def DecTohexString(number):
    return hex(number)


    



