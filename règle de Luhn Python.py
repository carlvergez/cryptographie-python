def vérif_Luhn:
    for i in range (1,16,2):
        double = 2*L[i]
        if double >9:
            double = 1 + double %10
        L[i]=double
    résultat =0
    for i in range (16):
        résultat = résultat + L[i]
    if résultat %10 == 0
        return (True)