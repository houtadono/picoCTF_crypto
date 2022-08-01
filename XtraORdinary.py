from random import randint
from pwn import xor
# fuction encrypt = decrypt = xor
ptxt = '57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637'
# ptxt is hex string
# and i see random_strs is list of bytes
ptxt = bytes.fromhex(ptxt)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

while 1:
    # xor(a,b) = c -> xor(a,c) = b
    # so loop is useless, only keep :for m in range(randint(0,pow(2,0)))
    # because randint(0,1) = 0 or 1; 
    # if m = 0, ptxt dont xor with key=random_str; if m = 1, ptxt do
    for random_str in random_strs:
        for m in range(randint(0,pow(2,0))):
            ptxt = xor(ptxt, random_str)

    # xor(flag,key) = ptxt -> xor(flag,ptxt) = key
    # flag start with 'picoCTF{'

    # flag_start = b'picoCTF{'
    # key = xor(ptxt[:len(flag_start)],flag_start)
    # using that code,brute-fore and i find key = Africa!
    # and continue using brute-fore find flag
    key = b'Africa!'
    flag = xor(ptxt,key).decode()
    if flag.startwith('picoCTF'):
        print(flag) # picoCTF{w41t_s0_1_d1dnt_1nv3nt_x0r???}