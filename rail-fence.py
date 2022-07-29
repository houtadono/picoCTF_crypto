
ciphertext = 'Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA'
key = 4 

def decryptRailFence(c = ciphertext,k = key):
    # create the matrix to cipher
    
    # key = rows ,
    # length(ciphertext) = columns
    rail = [ ['_' for j in range( len(c))] for i in range(k)]

    # mark the location of the ciphertext with '*'
    dir_down = False # check the direction up or down
    row, col = 0, 0 # find the direction with row,col
    for i in range(len(c)):
        rail[row][col] = '*'
        col+=1
        if row == 0 : dir_down = True
        if row == k-1   : dir_down = False

        if dir_down: row+=1 
        else: row-=1

    # replace '*' with ciphertext
    index = 0
    for i in range(k):
        for j in range(len(c)):
            if rail[i][j] == '*' and index < len(c):
                rail[i][j] = c[index]
                index += 1
    
    # read matrix in zigzag direction
    # result is plain text
    dir_down = False
    row, col = 0, 0
    plaintext = ""
    for i in range(len(c)):
        plaintext += rail[row][col]
        col+=1
        if row == 0 : dir_down = True
        if row == k-1   : dir_down = False

        if dir_down: row+=1 
        else: row-=1
    
    return plaintext

print(decryptRailFence()) # The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3
# picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}
