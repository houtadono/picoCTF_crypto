import requests
def factorDB(number):
    # using factordb.com to divide the number n into primes 
    # or u can install and import factorDB
    # method return a tuple (list_prime,boolean). boolean = True if n can into >1 prime.
    r = requests.get('http://factordb.com/index.php?query='+str(number))
    text_request = r.text

    list_prime = text_request.split('color="#000000">')[1:]
    list_prime = [ int(prime.split('</font>')[0]) for prime in list_prime]

    return list_prime, len(list_prime) > 1
