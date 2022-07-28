import codecs
# The first user in usernames.txt corresponds to the first password in passwords.txt

# in username.txt we find cultiris on line 278 
# so find password is cvpbPGS{P7e1S_54I35_71Z3}
ciphertext = 'cvpbPGS{P7e1S_54I35_71Z3}'

# flag: picoCTF.... ; p - c = 13 so we encode Rot 13
message = codecs.encode(ciphertext,'rot_13')

print(message) # picoCTF{C7r1F_54V35_71M3}