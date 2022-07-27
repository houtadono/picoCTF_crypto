import codecs

def encryptRot(plain,rot):
    enc =""
    for i in range(len(plain)):
        c = ord(plain[i])
        if(c>=65 and c <=90):
            c+=rot
            if(c>90): c-=26
        if(c>=97 and c <=122):
            c+=rot
            if(c>122): c-=26
        enc += chr(c)
    return enc

plainText = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
print(codecs.encode(plainText,'rot_13'))
flag = encryptRot(plainText,13)
print(flag)