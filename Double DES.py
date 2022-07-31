from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import DES
import binascii

def pad(msg): 
    block_len = 8
    over = len(msg) % block_len  
    pad = block_len - over 
    return (msg + " " * pad).encode()

FLAG = '8f2195680c2cc76698ed6f5f83f2b0dbec392af88346e2f55de120228c9e89f891a618091077c0b1'
KEY1 = KEY2 = ''
msgTest = '0123456701234567' #send to challenge and receive cirTest
cirTest = 'a1927f9b2969772191a618091077c0b1' # be encrypted twice
# decrypt one cirText with key 2 = encrypt one cirText with key 1

def double_encrypt(m):
    msg = pad(m)
    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    return cipher2.encrypt(enc_msg)

def double_decrypt(m):
    dec2 = DES.new(KEY2, DES.MODE_ECB)
    m = dec2.decrypt(m)
    dec1 = DES.new(KEY1, DES.MODE_ECB)
    return dec1.decrypt(m)

def single_encrypt(m,key):
    msg = pad(m)
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(msg)

def single_decrypt(m,key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(m)

def padKey(key):
    return pad(str(key).zfill(6))

FLAG = bytes.fromhex(FLAG)
msgTest = binascii.unhexlify(msgTest).decode()
cirTest = bytes.fromhex(cirTest)

# single_encrypt msgTest with Key1 -> dataEn1
dataEn1 = {}
for i in range(1000000):
    key1 = padKey(i)
    dataEn1[single_encrypt(msgTest,key1)] = key1

# single_decrypt cirTest with Key2 -> dec2
# and if dec2 in dataEn1:  key1,key2 True
listKey1Key2 = []
for i in range(1000000):
    key2 = padKey(i)
    try:
        dec2 = single_decrypt(cirTest,key2)
        if dec2 in dataEn1.keys():
            listKey1Key2.append({dataEn1[dec2],key2})
    except:
        continue

# using key1key2 true  
# double_decrypt Flag or single_decrypt((single_decrypt(Flag,key2)),key1)
for i in listKey1Key2:
    i = list(i)
    KEY1 = i[0]
    KEY2 = i[1]
    if double_encrypt(msgTest) == cirTest:
        print(double_decrypt(FLAG).decode()) # FLAG = cb120914153b84dbc68fedd574b395f2

