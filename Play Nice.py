# nc mercury.picoctf.net 6057
# Here is the alphabet: meiktp6yh4wxruavj9no13fb8d027c5glzsq
# Here is the encrypted message: y7bcvefqecwfste224508y1ufb21ld
# What is the plaintext message? 

alphabet = 'meiktp6yh4wxruavj9no13fb8d027c5glzsq'
enc_msg =  'y7bcvefqecwfste224508y1ufb21ld'

SQUARE_SIZE = 6
def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def decrypt_pair(pair,matrix):
    e1 = e2 = []
    for row in range(SQUARE_SIZE):
        for coil in range(SQUARE_SIZE):
            if( pair[0]==matrix[row][coil] ):
                e1 = [row,coil]
            if( pair[1]==matrix[row][coil] ):
                e2 = [row,coil]
    if e1[0] == e2[0]:
        return  matrix[e1[0]][(e1[1] - 1) % SQUARE_SIZE] + matrix[e2[0]][(e2[1] - 1) % SQUARE_SIZE]
    elif e1[1] == e2[1]:
        return  matrix[(e1[0] - 1) % SQUARE_SIZE][e1[1]] + matrix[(e2[0] - 1) % SQUARE_SIZE][e2[1]]
    else:
        return matrix[e1[0]][e2[1]] + matrix[e2[0]][e1[1]]

def decrypt_string(s,matrix):
    result = ""
    for i in range(0,len(s),2):
        result += decrypt_pair(s[i:i+2],matrix)
    return result

mt = generate_square(alphabet)
msg = decrypt_string(enc_msg,mt)

print(msg) # msg = wd9bukbspdtj7skd3kl8d6oa3f03g0

#send msg to What is the plaintext message? , we receive:
# Congratulations! Here's the flag: 2e71b99fd3d07af3808f8dff2652ae0e
