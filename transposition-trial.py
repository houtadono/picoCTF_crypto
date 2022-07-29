
ciphertext = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7'
# a block of 3 is : heT,f g, as, ii,cpC,CTo,...; 
# len ciphertext = 54 =>> so have 18 blocks
blocks = [ ciphertext[i:i+3] for i in range(0,len(ciphertext),3) ]

# see how the first block is scrambled: heT -> The
plaintext = "".join([ i[2] + i[0:2] for i in blocks ])
print(plaintext)
# The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}