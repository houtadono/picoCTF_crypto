from pwn import * 
import string

# u can send 1,11,11,111,111,111,... to know
# and send p recv data in flag

r = remote('mercury.picoctf.net',4572)
r.recvuntil('flag: ')
cipherFlag = r.recvline().decode()
n = r.recvline() # recv n
r.recvline() # recv e

flag = ''
alphabet = string.ascii_letters+string.digits+"{_}"

data_char = []
while 1:
    if flag.endswith('}'): break
    true_char = ""
    for char in alphabet:
        try:
            data = flag+char
            r.recvuntil('give me: ')
            r.sendline(data)
            r.recvuntil('you go: ')
            enc_flag = r.recvline().decode().replace("\n","")
            for i in data_char:
                enc_flag = enc_flag.replace(i,"")
            if enc_flag in cipherFlag:
                true_char = char
                data_char.append(enc_flag)
                break
        except:
            print("ReConnect.......")
            r = remote('mercury.picoctf.net',4572)
            r.recvuntil('flag: ')
            cipherFlag = str(r.recvline().decode())
            n = r.recvline() # recv n
            r.recvline() # recv e
            data = ''
            data_char = []
            for i in flag: 
                data += i
                r.recvuntil('give me: ')
                r.sendline(data)
                r.recvuntil('you go: ')
                enc_flag = r.recvline().decode().replace("\n","")
                for j in data_char:
                    enc_flag=enc_flag.replace(j,"")
                data_char.append(enc_flag)
    flag+=true_char
    print("flag: ",flag)
    # picoCTF{bad_1d3a5_3525501}
r.close() 



