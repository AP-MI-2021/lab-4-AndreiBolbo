import math
from math import sqrt,trunc
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
    lst3=[]
    for element in lst1:
         if element in lst2 and element not in lst3:
             lst3.append(element)
    return lst3


def test_intersectie():
    assert intersectia([1, 2, 3, 4], [2, 3, 4, 1])==[1, 2, 3, 4]
    assert intersectia([1, 2, 3, 4], [2, 2, 4, 1]) == [1, 2, 4]
    assert intersectia([1, 2, 3, 4], [5, 6, 7, 8]) == []

def main():
    lst1 = []
    lst2=[]
    while True:
        print("1. Citire a celor doua multimi intregi")
        print("2. Afisarea daca cele doua multimi au acelasi numar de elemente pare")
        print("3. Afisarea intersectiei celor doua multimi")
        print("4. Afisarea numerelor cu partea fractionara palindrom")
        print("5. Afisarea listei obtinute prin inversarea ca string a floaturilor cu "
              "partea intreaga a radicalului nr prim ")
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

test_nr_pare()
test_intersectie()
main()
