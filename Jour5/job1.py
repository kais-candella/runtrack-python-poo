def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

num = int(input("Entrez un nombre : "))
print("La factirielle de ", num ,"est",factorielle(num))
