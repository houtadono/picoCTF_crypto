from _mini_modules import encryptRot

message = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}'
key = 'CYLAB'
# with Vigenere: table(key + plaintext) = ciphertext; but plaintext && key only alpha
ciphertext = "".join([ i for i in message if i.isalpha() ])
key = key*(len(ciphertext)//len(key)+1)

# create table Vigen
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
table = []
for i in range(26):
    table.append(encryptRot(alphabet,i))

# decrypt
plaintext = ""
for i in range(len(ciphertext)):
    j = ciphertext[i]
    if j.isalpha():
        j = chr(table[ord(key[i])-65].find(j.upper()) + 65)
        if ciphertext[i].islower(): j = j.lower()
    plaintext += j


# add num,{},_ join plaintext -> flag
flag = ""
num = 0
for i in range(len(message)):
    if message[i].isalpha():
        flag += plaintext[num]
        num +=1
    else: flag += message[i]

print(flag) # picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}
