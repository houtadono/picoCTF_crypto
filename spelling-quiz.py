# this is Cipher Identifier
# and with this code:

import random
alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet,shuffled))

# we guess this is Mono-alphabetic Substitution

# so we use Mono-alphabetic Substitution Decoder
# we copy flag + study-guide -> 1 string and send about 100 line to web

flag = 'picoCTF{perhaps_the_dog_jumped_over_was_just_tired}'
print(flag)