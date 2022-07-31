import string
import zlib
from pwn import *

# like as name challenger, we look compress
def compress(text):
    return zlib.compress(bytes(text.encode("utf-8")))

# if u compress('aabb')= x and  compress('aaaa')= y: len(x) < len(y) 
# so usr_input = FLAG : picoCtf{....} is True and have (len(encrypted_text) is min)

# we will brute-force any satisfying character and send to challenger
alphabet = string.ascii_letters+string.digits+"_}"
FLAG = 'picoCTF{sher'

r =  remote("mercury.picoctf.net", 50899)
while 1:
    if FLAG[-1] == '}':
        r.close()
        break
    len_min,true_char = 1000,'a'
    for char in alphabet:
        try:
            data = FLAG + char
            r.recvuntil("encrypted: ")  
            r.sendline(data)
            r.recvline() 
            r.recvline()
            len_cipher = int(r.recvline().decode())
            if len_min > len_cipher:
                len_min,true_char = len_cipher,char
        except:
            r =  remote("mercury.picoctf.net", 50899) # running time is quite long,
            # so connection may be lost
    FLAG += true_char
    print("FLAG: ",FLAG) # FLAG:  picoCTF{sheriff_you_solved_the_crime}
