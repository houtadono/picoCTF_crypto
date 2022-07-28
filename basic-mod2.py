from Crypto.Util.number import inverse
ciphertext = "104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377".split(" ")
ciphertext = [ inverse(int(i),41) for i in ciphertext]
message = ""
for i in ciphertext:
    c = ""
    if i == 0 or i>37: continue
    if i < 27 :
        c = chr(96+i)
    elif i == 37:
        c = '_'
    else: c = str(i-27)
    message += c
print(message) # picoCTF{1nv3r53ly_h4rd_8a05d939}
