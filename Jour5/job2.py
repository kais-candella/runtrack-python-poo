def calcule(n,):
    if n == 0:
        return 1
    else:
        return 2 *calcule(n-1)

n = int(input("Entrez un nombre : "))
resulta = calcule(n)
print("2^{} = {}".format(n,resulta)) 