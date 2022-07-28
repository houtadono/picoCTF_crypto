ciphertext = "202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397".split(" ")
ciphertext = [ int(i)%37 for i in ciphertext]
message = ""
for i in ciphertext:
    c = ""
    if i < 26 :
        c = chr(97+i)
    elif i == 36:
        c = '_'
    else: c = str(i-26)
    message += c
print(message) # r0und_n_r0und_b6b25531
