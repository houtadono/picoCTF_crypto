import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
cipherText = 'kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm'

def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1-t2)%len(ALPHABET)]

def decrypt(enc,key):
    dec = ""
    for c in enc:
        dec += unshift(c,key)
    return dec

def b16_decode(enc):
    plain = ""
    for c1, c2 in zip(enc[0::2], enc[1::2]):
        n1 = "{0:04b}".format(ALPHABET.index(c1))
        n2 = "{0:04b}".format(ALPHABET.index(c2))
        binary = int(n1 + n2,2)
        plain += chr(binary)
    return plain

for key in ALPHABET: # because len(key) = 1
    decrypted = decrypt(cipherText,key)
    if all([c in ALPHABET for c in decrypted]):
        decoded = b16_decode(decrypted)
        if all([c in string.printable for c in decoded]):
            print(decoded) # PICOCTF{et_tu?_1ac5f3d7920a85610afeb2572831daa8}
            break