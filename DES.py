import random
#Initial Permutation Array
IP1 = ( 
        58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7, )
#Inverse Initial Permutation Array
IP2 = ( 
        40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25 )
s = ( 
        (
            ( 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7 ),
            ( 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8 ),
            ( 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0 ),
            ( 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 )
            ),
        (
            ( 15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10 ),
            ( 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5 ),
            ( 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15 ),
            ( 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 )
            ),
        (
            ( 10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8 ),
            ( 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1 ),
            ( 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7 ),
            ( 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 )
            ),
        (
            ( 7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15 ),
            ( 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9 ),
            ( 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4 ),
            ( 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 )
            ),
        (
            ( 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9 ),
            ( 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6 ),
            ( 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14 ),
            ( 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 )
            ),
        (
            ( 12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11 ),
            ( 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8 ),
            ( 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6 ),
            ( 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 )
            ),
        (
            ( 4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1 ),
            ( 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6 ),
            ( 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2 ),
            ( 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 )
            ),
        (
            ( 13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7 ),
            ( 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2 ),
            ( 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8 ),
            ( 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11 )
            )
        )
#Expand Array;
Ex = ( 
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1 )
#P-change Arra
P = ( 
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25 )

#PC-1 Array in keyBuild
PC1 = ( 
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 33, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4 )
#PC-2 Array in keyBuild
PC2 = ( 
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32 )

#generate 16 key
gkey = []
def gk(key):
    sb = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1) #shiftbit
    key64 = hexto2(key)
    key56 = []
    for i in range(56):
        key56.insert(i,key64[PC1[i]-1])
    for i in range(16):
        key56,temp = gk2(key56,sb[i])
        gkey.insert(i,temp)

def gk2(key56,flag):
    if flag == 1:
        key56 = key56[1:28]+key56[:1]+key56[29:56]+key56[28:29]
    elif flag == 2:
        key56 = key56[2:28]+key56[:2]+key56[30:56]+key56[28:30]
    return key56,[key56[PC2[i]-1] for i in range(48)]

# 16进制->2进制
def hexto2(key): # return a int list 
    key64 = bin(int(key,16))[2:]
    while len(key64) < 64 : key64 = '0'+key64
    return [int(i) for i in list(key64)]


def inip(text): #initial permutation
    text64 = hexto2(text)
    lis = [text64[IP1[i]-1] for i in range(64)]
    return lis[:32],lis[32:]


def invp(text): #return string list / char list
    return [str(text[IP2[i]-1]) for i in range(64)]

# ri list 32 
def expandr(ri):
    return [ri[Ex[i]-1] for i in range(48)]


#ri 32 ki 48
def f(ri,ki):
    ri = expandr(ri)
    nlis = [str(ri[i]^ki[i]) for i in range(48)] # str list
    ans = ''
    for i in range(8):
        tlis = nlis[i*6:i*6+6]
        temp = bin(s[i][int(tlis[0]+tlis[5],2)][int(tlis[1]+tlis[2]+tlis[3]+tlis[4],2)])[2:]
        while len(temp) < 4: 
            temp = '0'+temp
        ans += temp
    ri = [int(ans[i]) for i in range(32)]
    return [ri[P[i]-1] for i in range(32)]

def encode(text,key,flag = 1,cnt = 16):
    gk(key)  #generate 16 keys
    le,ri = inip(text)
    for i in range(cnt):
        temp = ri
        if flag == 1 : ri = f(ri,gkey[i]) #encode
        else: ri = f(ri,gkey[cnt-1-i]) #decode 将密钥反过来用
        ri = [ ri[j] ^ le[j] for j in range(32) ]
        le = temp
    ans = invp(ri+le)#str list
    anss,temps = '',''
    for i in range(64):
        temps += ans[i]
        if len(temps) == 8:
            tt = hex(int(temps,2))[2:]
            while len(tt) < 2: tt = '0'+tt
            anss += tt
            temps = ''
    return anss
#flag 从右数的位数
def randomgai(t,flag = -1):
    if flag == -1 :
        temp = random.randint(1,64)
    else:
        temp = flag
    t64 = bin(int(t,16))[2:]
    while len(t64) < 64 : t64 = '0'+t64
    t64 = int(t64,2)
    t64 = t64 ^ (1<<(temp-1))
    t16 = hex(t64)[2:]
    while len(t16) < 16 : t16 = '0'+t16
    return t16

def encodeAll(text,key):
    t16All=''
    for i in range(len(text)):
        if (i+1)%16==0:
            temp=encode(text[i-15:i+1],key)
            t16All=t16All+temp
    return t16All

def decodeAll(text,key):
    t16All=''
    for i in range(len(text)):
        if (i+1)%16==0:
            temp=encode(text[i-15:i+1],key,2)
            t16All=t16All+temp
    return t16All


  

