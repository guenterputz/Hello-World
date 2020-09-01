from random import shuffle

liste = "amazing really excited stunning bold delightful fantastic phenomenal ambitious \
biggest best gorgeous outstanding staggering tremendous exciting".upper().split()
shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM ",end= "")
        print()
    el1 = liste.pop()
    el2 = liste.pop()

    print("{} SPAM,{} SPAM".format(el1,el2))
    print()