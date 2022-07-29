# in file message.txt, we can divide it into 3 parts

key = "VOUHMJLTESZCDKWIXNQYFAPGBR" 
message = "Tmnmfiwk Cmlnvkh vnwqm, peyt v lnvam vkh qyvymcb ven, vkh onwflty dm ytm ommycm\n\
jnwd v lcvqq uvqm ek pteut ey pvq mkucwqmh. Ey pvq v omvfyejfc quvnvovmfq, vkh, vy\n\
ytvy yedm, fkzkwpk yw kvyfnvceqyq—wj uwfnqm v lnmvy inerm ek v quemkyejeu iweky\n\
wj aemp. Ytmnm pmnm ypw nwfkh ocvuz qiwyq kmvn wkm mgynmdeyb wj ytm ovuz, vkh v\n\
cwkl wkm kmvn ytm wytmn. Ytm quvcmq pmnm mgummheklcb tvnh vkh lcwqqb, peyt vcc ytm\n\
viimvnvkum wj ofnkeqtmh lwch. Ytm pmelty wj ytm ekqmuy pvq amnb nmdvnzvocm, vkh,\n\
yvzekl vcc yteklq ekyw uwkqehmnvyewk, E uwfch tvnhcb ocvdm Sfieymn jwn teq wiekewk\n\
nmqimuyekl ey."
flag = 'Ytm jcvl eq: ieuwUYJ{5FO5717F710K_3A0CF710K_357OJ9JJ}'

# key looks like alphabet 1-1, so we can decrypt message && flag ez

def decryptMonoAlphabetSubstitution(c,dic):
    plain = ""
    for i in c:
        if str(i).isalpha():
            if str(i).islower: i = str(dic[str(i).upper()]).lower()
            else:i = dic[str(i)]
        plain+=i
    return plain

alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
dic = dict(zip(key,alphabet))

print(decryptMonoAlphabetSubstitution(message,dic))
# hereupon legrand arose, with a grave and stately air, and brought me the beetle
# from a glass case in which it was enclosed. it was a beautiful scarabaeus, and, at
# that time, unknown to naturalists—of course a great prize in a scientific point
# of view. there were two round black spots near one extremity of the back, and a
# long one near the other. the scales were exceedingly hard and glossy, with all the
# appearance of burnished gold. the weight of the insect was very remarkable, and,
# taking all things into consideration, i could hardly blame jupiter for his opinion
# respecting it
print(decryptMonoAlphabetSubstitution(flag,dic))
#the flag is: picoctf{5ub5717u710n_3v0lu710n_357bf9ff}
