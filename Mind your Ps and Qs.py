from Crypto.Util.number import inverse , long_to_bytes
from _mini_modules import factorDB

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

# Decrypt RSA: with publicKey = [n,e] , cipherText = c
list_prime = factorDB(n)[0]
phi = 1
for prime in list_prime:
    phi *= prime -1

d = inverse(e,phi)
message = pow(c,d,n)
print(long_to_bytes(message).decode()) # picoCTF{sma11_N_n0_g0od_23540368}