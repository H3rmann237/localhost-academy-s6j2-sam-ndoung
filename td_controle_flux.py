# ====== ===== ===== ===== ===== ====== =====
# EXERCICE 1
# ====== ===== ===== ===== ===== ====== =====

#note = input("entrez la note /20 : ")

#note_float = float(note)

#if note_float >= 16 :
#    print("Excellent")
#elif note_float >= 12 :
#    print("Bien")
#else :
#    print("Insuffisant")

# ====== ===== ===== ===== ===== ====== =====
# EXERCICE 2
# ====== ===== ===== ===== ===== ====== =====

#for i in range (1 , 11) :
#    print (i , i ** 2)

# a- la boucle n'affiche pas 11 ligne car range ne lit pas 11 mais plutot 11-1 donc 10 éléments

#for a in range(0,21,2):
#    print(a)

#total = 0
#for b in range(1,101):
#    total += b
#print(total)

# ====== ===== ===== ===== ===== ====== =====
# EXERCICE 3
# ====== ===== ===== ===== ===== ====== =====

#mdp = "python2026"
#mdp_user = input("Entrez le mot de passe : ")
#left_try = 3

#while True:
#    if mdp_user == mdp :
#        print("Acces autorise !")
#        break
#    else:
#        left_try -= 1
#        print(f"Incorrect , il vous reste {left_try} tentative(s).")
#    if left_try != 0:
#        mdp_user = input("Entrez le mot de passe : ")
#    else :
#        print("Compte bloque.")
#        break

# ====== ===== ===== ===== ===== ====== =====
# EXERCICE 4
# ====== ===== ===== ===== ===== ====== =====
def  est_pair(n) :
    if n%2 == 0:
        return print("True")
    else :
        return print("False")

def maximum(a, b) :
    if a > b :
        return print(a)
    else :
        return print(b)
    
def compter_voyelles(mot) :
    nbr_voyelle = 0
    for i in mot:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
            nbr_voyelle += 1
    return print(nbr_voyelle)

est_pair(4)
maximum(6, 2)
compter_voyelles("azerty")