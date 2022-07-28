
ciphertext = 'UFJKXQZQUNB' 
key        = 'SOLVECRYPTO'
# using table.txt
# or we code table and decrypt ciphertext
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

alphabet ='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.replace(' ','')
table = []
for i in range(26):
    table.append(encryptRot(alphabet,i))


message =""
for i,j in zip(ciphertext,key):
    message += alphabet[table[ord(j)-65].find(i)]
    # ex: key S, cipher U
    #      C
    #  S   U 
    #   -> message C
print(message) # CRYPTOISFUN