import codecs

def decryptRot(cipher,rot):
    result = []
    for i in range(len(cipher)):
        c = ord(cipher[i])
        if(c>=65 and c<=90): 
            c-=rot
            if c<65: c+=26
        if(c>=97 and c<=122): 
            c-=rot
            if c<97: c+=26    
        result.append(chr(c))

    return "".join(result)

cipherText = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"

flag = decryptRot(cipherText,13)
print(flag)

print(codecs.decode(cipherText,'rot_13'))