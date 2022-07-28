import requests
from Crypto.Util.number import inverse,long_to_bytes
cipherText = publicKey = module = ''

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

def factorDB(number):
    # using factordb.com to divide the number n into primes 
    # or u can install and import factorDB
    # method return a tuple (list_prime,boolean). boolean = True if n can into >1 prime.
    r = requests.get('http://factordb.com/index.php?query='+str(number))
    text_request = r.text

    list_prime = text_request.split('color="#000000">')[1:]
    list_prime = [ int(prime.split('</font>')[0]) for prime in list_prime]

    return list_prime, len(list_prime) > 1
    
def iroot(x, n):
        """Return (y, b) where y is the integer nth root of x and b is True if y is exact."""
        if x == 0:
            return x, True

        k = (x.bit_length() - 1) // n
        y = 1<<k
        for i in range(k-1, -1, -1):
            z = y | 1<<i
            if z**n <= x:
                y = z
        return y, x == y**n 

def decryptRSA(c = cipherText,e = publicKey, n = module):
    list_prime = factorDB(n)[0]
    phi = 1
    for prime in list_prime:
        phi *= prime -1

    d = inverse(e,phi)
    message = pow(c,d,n)
    return long_to_bytes(message).decode()

