from cmath import sqrt
import math

def is_interger(lst):
    lst_int = []
    for nr in lst:
        if nr == int(nr):
            lst_int.append(int(nr))
    return lst_int


def highest_divk(lst, k):
    maxd = None
    for nr in lst:
        if nr % k == 0:
            if maxd is None or nr > maxd:
                maxd = nr
    return maxd


def extract_fractionary(n):
    return str(n).split('.')[1]


def is_palindrome(n):
    p = 0
    cn = n
    while n:
        p = p*10 + n%10
        n=n//10
    return cn==p


def palindrome(lst):
    lst_p=[]
    for nr in lst:
        frac=extract_fractionary(nr)
        if is_palindrome(int(frac)):
            lst_p.append(nr)
    return lst_p


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def invert_floats_with_sqrt_of_int_prim(lista):
    result = []

    for numar in lista:
        sqrt_nr = sqrt(numar)
        sqrt_int = math.trunc(sqrt_nr)
        if is_prime(sqrt_int):
            numar_str = invert_float_as_string(numar)
            result.append(numar_str)
        else:
            result.append(numar)

    return result


def invert_float_as_string(numar):
    numar_str = str(numar)
    return numar_str[::-1]


def main():
    lst = []
    while True:
        print("1. Citire lista float")
        print("2. Afisarea tuturor numerelor intregi")
        print("3. Afisarea celui mai mare numar dvizibil cu un numar dat")
        print("4. Afisarea numerelor cu partea fractionara palindrom")
        print("5. Afisarea listei obtinute prin inversarea ca string a floaturilor cu "
              "partea intreaga a radicalului nr prim ")
        print("x. Pentru a iesi din program")
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            lst_string = input("dati numerele separate prin spatiu :")
            lst_sep = lst_string.split(' ')
            for nr in lst_sep:
                lst.append(float(nr))
        elif optiune == '2':
            lst_i = is_interger(lst)
            print(lst_i)
        elif optiune == 'x':
            break
        elif optiune == '3':
            k = int(input("dati k:"))
            max_k = highest_divk(lst, k)
            if max_k is None:
                print("Nu exista niciun nr divizibil cu k")
            else:
                print(max_k)
        elif optiune == '4':
            lst_pal = palindrome(lst)
            print(lst_pal)
        elif optiune == '5':
            invert_floats_with_sqrt_of_int_prim(lst)

main()
