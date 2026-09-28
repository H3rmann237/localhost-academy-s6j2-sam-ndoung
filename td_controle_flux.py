# ====== ===== ===== ===== ===== ====== =====
# EXERCICE 1
# ====== ===== ===== ===== ===== ====== =====

#note = input("entrez la note /20 : ")

#note_float = float(note)

#if (note_float >= 16):
#    print("Excellent")
#elif (note_float >= 12):
#    print("Bien")
#else :
#    print("Insuffisant")

# ====== ===== ===== ===== ===== ====== =====
# EXERCICE 2
# ====== ===== ===== ===== ===== ====== =====

for i in range (1 , 11) :
    print (i , i ** 2)

# a- la boucle n'affiche pas 11 ligne car range ne lit pas 11 mais plutot 11-1 donc 10 éléments

for a in range(0,21,2):
    print(a)

total = 0
for b in range(1,101):
    total += b
print(total)