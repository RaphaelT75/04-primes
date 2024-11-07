"""
dans ce module on cherche à déterminer si un nombre est premier 
pour cela on utilise une fonction secondaire qui se charge de déterminer si le nombre est premier
et une fonction secondaire qui s'occupe de tester
"""
from math import sqrt
def isprime(p):
    """
    Fonction qui permet de déterminer si un nombre est premier.
    On teste avec une boucle for si il existe un autre diviseur si oui on renvoi faux
    Si aucun diviseur n'a été trouvé, alors il est premier
    """
    if sqrt(p*p) <= 1 :
        return False
    for d in range(2,p) :
        if  sqrt(p*p) % d == 0 :
            return False
    return True
def main():
    """
    fonction main qui sert à tester isprime
    """
    print("Tests spécifiques:")
    print(f"-6 est premier : {isprime(-6)}")
    print(f"0 est premier : {isprime(0)}")
    print(f"1 est premier : {isprime(1)}")
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
