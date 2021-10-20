import math
from math import sqrt, trunc


def nr_pare(lst):
    """
    functia determina numarul de elemente pare dintr o lista
    input:lst:list[int]
    return: nr(numarul elementelor pare)
    """
    nr=0
    for element in lst:
        if element % 2 == 0:
            nr += 1
    return nr
def multimi_pare(lst1, lst2):
    """
    verifica daca cele doua liste au acelasi numar de elemente pare
    :param lst1:
    :param lst2:
    :return: True/False
    """
    nr_pare1 = nr_pare(lst1)
    nr_pare2 = nr_pare(lst2)
    if nr_pare1 == nr_pare2:
        return True
    return False


def test_nr_pare():
    assert multimi_pare([1, 2, 3, 4], [2, 3, 4, 1]) == 1
    assert multimi_pare([1, 2, 3, 4], [2, 3, 4, 2]) == 0
    assert multimi_pare([1, 2, 2, 4], [2, 2, 4, 1]) == 1


def intersectia(lst1,lst2):
    """
    verifica daca un element din prima lista se regaseste in cealalta iar daca da il adauga in lista de intersectie
    :param lst1:
    :param lst2:
    :return:lst3 (lista intersectiei)
    """
    lst3 = []
    for element in lst1:
         if element in lst2 and element not in lst3:
             lst3.append(element)
    return lst3


def test_intersectie():
    assert intersectia([1, 2, 3, 4], [2, 3, 4, 1])==[1, 2, 3, 4]
    assert intersectia([1, 2, 3, 4], [2, 2, 4, 1]) == [1, 2, 4]
    assert intersectia([1, 2, 3, 4], [5, 6, 7, 8]) == []

def palindrom(n):
    """
    construieste oglinditul numarului urmand sa il verifice cu valoarea initiala iar astfel verifica daca e palindrom
    :param n:
    :return: True/False
    """
    x=n
    p=0
    while x:
        p=p*10+x%10
        x=x//10
    if p==n:
        return True
    return False


def concatenare(lst1,lst2):
    """
    concateneaza elementele de pe aceleasi pozitii din sir
    :param lst1:
    :param lst2:
    :return: lst3 (lista concatenata)
    """
    lst3=[]
    if len(lst1)<=len(lst2):
        n=len(lst1)
    else:
        n=len(lst2)
    for i in range(n):
        v=str(lst1[i])
        c=str(lst2[i])
        t=v+c
        lst3.append(int(t))
    return lst3


def verif_lista(lst):
    """
    verifica elementele din lista care sunt palindrom punandu-le intr-o noua lista
    :param lst:
    :return: lst4 (lista tuturor palindroamelor)
    """
    lst4=[]
    for element in lst:
        if palindrom(element):
            lst4.append(element)
    return lst4

def test_concatenare():
    assert concatenare([12, 22, 36, 11],[21, 23, 63, 55, 424])==[1221,2223,3663,1155]


def test_verif_lista():
    assert verif_lista([1221,2223,3663,1155])==[1221,3663]
    assert verif_lista([2223,1155])==[]


def divizibil_k(lst,k):
    for element in lst:
        if element % k ==0:
            return True
    return False


def oglindit(n):
    x = n
    p = 0
    while x:
        p = p * 10 + x % 10
        x = x // 10
    return p

def divizibila_cu_lista(lst1,lst3):
    for element in lst3:
            if divizibil_k(lst1,element)==0:
                return False
    return True


def oglindire(lst1,lst3):
    lst4=[]
    if divizibila_cu_lista(lst1,lst3):
        for element in lst1:
            lst4.append(oglindit(element))
    else:
        lst4=lst1

def main():
    lst1 = []
    lst2=[]
    while True:
        print("1. Citire a celor doua multimi intregi")
        print("2. Afisarea daca cele doua multimi au acelasi numar de elemente pare")
        print("3. Afisarea intersectiei celor doua multimi")
        print("4. Afisarea tuturor palindroamelor obtinute prin concatenarea elementelor din cele doua liste aflate pe aceleasi pozitii")
        print("5. Afisarea listei oglindite pentru care toate elementele multimii c divid multimile a si b ")
        print("x. Pentru a iesi din program")
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            lst_string = input("dati numerele separate prin spatiu a primei multimi:")
            lst_sep = lst_string.split(' ')
            for nr in lst_sep:
                lst1.append(int(nr))
            lst_string = input("dati numerele separate prin spatiu a celei de a doua multimi:")
            lst_sep = lst_string.split(' ')
            for nr in lst_sep:
                lst2.append(int(nr))
        elif optiune == '2':
            if multimi_pare(lst1,lst2):
                print("Au acelasi numar de elemente pare")
            else:
                print("Nu au acelasi numar de elemente pare")

        elif optiune == 'x':
            break
        elif optiune == '3':
            lst3=intersectia(lst1,lst2)
            if len(lst3):
                print(lst3)
            else:
                print("nu exista elemente in intersectie")
        elif optiune == '4':
            lst3=concatenare(lst1,lst2)
            lst4=verif_lista(lst3)
            if len(lst3):
                print(lst4)
            else:
                print("nu exista elemente palindrom obtinute")
        elif optiune =='5':
            lst3=[]
            lst_string = input("dati numerele separate prin spatiu a primei multimi:")
            lst_sep = lst_string.split(' ')
            for nr in lst_sep:
                lst3.append(int(nr))



test_nr_pare()
test_intersectie()
test_concatenare()
test_verif_lista()
main()
