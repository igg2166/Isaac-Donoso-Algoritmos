#Invertir un String
#hola --> aloh


def invertir_palabra_recursiva(palabra):
    if len(palabra) <= 1:
        return palabra
    return invertir_palabra_recursiva(palabra[1:]) + palabra[0]

print(invertir_palabra_recursiva("hola"))

def palabra_invertida(palabra):
    while palabra:
        return   

saludo = "hola"

saludo_invertido = saludo[::-1]

print(saludo_invertido)

def reconocer_palindromo(palabra):
    palindromo = invertir_palabra_recursiva(palabra)

    if palindromo == palabra:
        print(f"La palabra {palabra} es un palindromo")
    else:
        print(f"La palabra {palabra} no es un palindromo")

def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return palindromo(palabra[1:-1])
    else:
        return False
    
palabra = "hola"
palabra_palindromo = palindromo(palabra)

if palabra_palindromo:
    print(f"La palabra {palabra} es un palindromo")
else:
    print(f"La palabra {palabra} no es un palindromo")

#Contar cuantas veces se repite un caracterer en un texto

def caracteres_repetidos(palabra, caracter):
    if len(palabra) == 0:
        return 0
    if palabra[0] == caracter:
        return 1 + caracteres_repetidos(palabra[1:], caracter)
    else:
        return caracteres_repetidos(palabra[1:], caracter)

def caracteres_repetidos_profe(palabra, caracter):
    if len(palabra) == 0:
        return 0

    cuenta = 1 if palabra[0] == caracter else 0
    return cuenta + caracteres_repetidos_profe(palabra[1:], caracter)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def contar_nodos_recursivos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos_recursivos(nodo.siguiente)
    
    def contar_nodos(self):
        return self.contar_nodos_recursivos(self.cabeza)

#Metodo recursivo que diga la longuitud de un lista

def longuitud_lista(lista: list):
    if lista is None:
        return 0
    lista = lista.pop()
    return 1 + longuitud_lista(lista)

lista = {1,2,3,4,5}

print(longuitud_lista(lista))