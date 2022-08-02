from _mini_modules import iroot
from Crypto.Util.number import long_to_bytes

# attack RSA with small e, same e
# m(message) =flag , send m to e times:
# c1 = pow(m,e,n1) c2 = pow(m,e,n1) c3 = pow(m,e,n1)

# M = pow(m,e) : e =3 , M = m ** 3
# -> M = c1 mod n1; M = c2 mod n2; M = c3 mod n3

# using Chinese Remainder Theorem find M and m = iroot(M,e)
def Chinese_Remainder(c,mod): 
    res = 0
    volume = 1
    for i in mod:
        volume*=i
    for (i,j) in zip(c,mod):
        m = volume//j
        res += i*m*pow(m,-1,j)
    return res%volume

data = []
with open('encrypted-messages.txt', 'rb') as f:
    data = f.read().decode().split("\n\n")

#  because encrypt use random.shuffle
combination = []
K = 3
N = len(data) 
pos = []
for i in range(N+1):
    pos.append(0)
def tryCom(i):
    for j in range(pos[i-1]+1,N-K+i+1,1):
        pos[i] = j
        if i == K:
            combination.append(pos[1:K+1])
        else: tryCom(i+1)

tryCom(1) # combination = [[1,2,3],[1,2,4],[1,2,5],....,[10,11,12]]

#brute-force
for pos in combination:
    rsa = [data[i-1] for i in pos]
    listCipher = []
    listModule = []
    for i in rsa:
        j = i.split("\n")
        n = int(j[0].split('n: ')[1])
        e = int(j[1].split('e: ')[1])
        c = int(j[2].split('c: ')[1])
        listCipher.append(c)
        listModule.append(n)
    M = Chinese_Remainder(listCipher,listModule)
    try:
        m = iroot(M,3)[0]
        plaintext = long_to_bytes(m).decode()
        print(plaintext)
    except: 
        continue
# I hope we win that big rowing match next week!
# picoCTF{1_gu3ss_p30pl3_p4d_m3ss4g3s_f0r_4_r34s0n}
# I just cannot wait for rowing practice today!
# Rowing is such a fun sport!