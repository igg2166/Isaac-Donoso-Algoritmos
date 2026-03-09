def formas_subir_memo(n, cache = {}):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if n in cache:
        return cache[n]

    cache[n] = formas_subir_memo(n-1, cache) + formas_subir_memo(n-2, cache)
    return cache[n]

def formas_subir(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return formas_subir(n-1) + formas_subir(n-2)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None   

class Pilas:
    def __init__(self):
        self.tope = None
        self.tamaño = 0

    def esta_vacia(self):
        return self.tope is None
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamaño += 1
        return nuevo

    def pop(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamaño -= 1
        return dato
    
    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato


def orden(expresion):
    mapa = {")":"(", "}":"{", "]":"["}
    apertura = set(mapa.values())
    cierre = set(mapa.keys())

    for token in expresion:
        if token in apertura:
            pila.push(token)
        elif token in cierre:
            if pila.esta_vacia():
                print("Error")
                break
            tope = pila.pop()
            if tope != mapa[token]:
                print("Error")  
    print("Exitoso")

    
pila = Pilas()
expresion = "({[]})"

orden(expresion)


#print(formas_subir(40))
#print(formas_subir_memo(750))