from _mini_modules import decryptRot

encrpyt = "picoCTF{ynkooejcpdanqxeykjrbdofgkq}".split('CTF{')[1].split('}')[0]
for i in range(26):
    message = "picoCTF{"
    print(i,message+decryptRot(encrpyt,i)+'}')
    # we look for a meaningful flag
    # 22 picoCTF{crossingtherubiconvfhsjkou}
