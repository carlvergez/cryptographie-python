alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choix = input("Voulez-vous encoder ou décoder un mot? ") 
print("Vous avez choisi d'",choix)
mot = input("Quel est le mot choisi?")
print("le mot choisi est:",mot)


def encodage (mot):
    n = len (mot)
    Nouveau_Mot = [0]*n
    for i in range (0,n): 
        indice = alphabet.index (mot[i])
        reste = (15*indice + 7)%26
        Nouveau_Mot[i]=alphabet[reste] 
    mot_caché = ''.join(Nouveau_Mot) #trasnforme les éléments d'une liste sous forme d'une chaine de caractères.
    return (mot_caché)
def décodage (mot):
    n = len (mot)
    Nouveau_Mot = [0]*n
    for i in range (0,n):
        indice = alphabet.index (mot[i])
        reste = (7*indice + 3)%26
        Nouveau_Mot[i]=alphabet[reste]
    mot_caché = ''.join(Nouveau_Mot)
    return (mot_caché)

if choix == "encoder":
    print (encodage(mot))

if choix == "décoder":
    print (décodage(mot))
#else:
    #print (décodage(mot))


