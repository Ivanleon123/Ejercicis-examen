"Ejercicis examen" 
def lleguir_llista_enters():
    llista = []  
    while True:
        entrada = input("Introdueix un nombre o '.' per acabar: ")
        if entrada == ".":
            break  
        try:
            numero = int(entrada)  
            llista.append(numero)  
        except ValueError:
            print("No has introduït un nombre vàlid. Torna-ho a intentar.") 
    return llista


def senars_llist(llista):
    llista_senars = []  
    for num in llista:
        if num % 2 != 0:  
            llista_senars.append(num)
    return llista_senars


def sumar_parells_llista(llista):
    suma = 0  
    for num in llista:
        if num % 2 == 0:  
            suma += num  
    return suma


def cercar_numero_llista(llista, numero):
    for i in range(len(llista)):  
        if llista[i] == numero:  
            return i  
    return -1  


def llegir_llista_paraules():
    llista = []  
    while True:
        entrada = input("Introdueix una paraula o '.' per acabar: ")
        if entrada == ".":
            break  
        llista.append(entrada)  
    return llista


def crear_funcio_llista(llista):
    inicials = ""  
    for paraula in llista:
        inicials += paraula[0]  
    return inicials


import random

def crear_llista_num_aleatori():
    llista = [random.randint(1, 100) for _ in range(5)]  
    return llista


def comparar_llistes(llista1, llista2):
    resultat = []  
    for i in range(len(llista2)):
        if llista2[i] == llista1[i]:  
            resultat.append(2)
        elif llista2[i] in llista1:  
            resultat.append(1)
        else:  
            resultat.append(0)
    return resultat


def majors_edat(edat1, edat2):
    resultat = []
    
    if edat1 >= 18:
        resultat.append("Edat1 és major d'edat")
    else:
        resultat.append("Edat1 no és major d'edat")
    
    if edat2 >= 18:
        resultat.append("Edat2 és major d'edat")
    else:
        resultat.append("Edat2 no és major d'edat")
    
    return resultat


def menu():
    print("Selecciona una opció:")
    print("1. Llegir llista d'enters")
    print("2. Filtrar els nombres senars d'una llista")
    print("3. Sumar els nombres parells d'una llista")
    print("4. Cercar un número en una llista")
    print("5. Llegir una llista de paraules")
    print("6. Crear una nova llista amb les inicials de les paraules")
    print("7. Crear llista amb 5 números aleatoris")
    print("8. Comparar dues llistes de 5 elements")
    print("9. Comprovar si dues persones són majors d'edat")
    
    opcio = int(input("Introdueix el número de l'opció que vols seleccionar: "))
    return opcio

