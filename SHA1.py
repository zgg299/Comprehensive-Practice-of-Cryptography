import hashlib
from fileclient import*
from fileserver import*

def sha1():
    sha1=hashlib.sha1()
    msg_to_hash1=readfile_plain()
    sha1.update(msg_to_hash1.encode('utf-8'))
    hashcode=sha1.hexdigest()
    return hashcode


