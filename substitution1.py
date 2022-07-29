from _mini_modules import decryptMonoAlphabetSubstitution
ciphertext = "OYAt (txwsy aws ompyksb yxb ajmf) msb m yupb wa owzpkybs tboksgyu owzpbygygwd. Owdybtymdyt msb psbtbdybr lgyx m tby wa oxmjjbdfbt lxgox ybty yxbgs osbmygegyu, yboxdgomj (mdr fwwfjgdf) tqgjjt, mdr pswhjbz-twjegdf mhgjgyu. Oxmjjbdfbt ktkmjju owebs m dkzhbs wa omybfwsgbt, mdr lxbd twjebr, bmox ugbjrt m tysgdf (omjjbr m ajmf) lxgox gt tkhzgyybr yw md wdjgdb towsgdf tbsegob. OYAt msb m fsbmy lmu yw jbmsd m lgrb mssmu wa owzpkybs tboksgyu tqgjjt gd m tmab, jbfmj bdegswdzbdy, mdr msb xwtybr mdr pjmubr hu zmdu tboksgyu fswkpt mswkdr yxb lwsjr aws akd mdr psmoygob. Aws yxgt pswhjbz, yxb ajmf gt: pgowOYA{AS3CK3DOU_4774OQ5_4S3_O001_6B0659AH}"
# use: https://www.guballa.de/substitution-solver
# we copy ciphertext (**remove the flag part) send to web 
# and receive key: mhorbafxgnqjzdwpcstykelvui 
key = 'mhorbafxgnqjzdwpcstykelvui'
print(decryptMonoAlphabetSubstitution(ciphertext,key)) # picoCTF{FR3QU3NCY_4774CK5_4R3_C001_6E0659FB}