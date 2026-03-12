def eliminar_duplicados(lista):
    lista_arreglada = []
    for e in lista:
        if e in lista_arreglada:
            print(f"El elemento {e} esta repetido en la lista")
        else:
            lista_arreglada.append(e)
    return lista_arreglada

def eliminar_duplicados_opti(lista):
    conjunto = list(set(lista))
    return conjunto

print(eliminar_duplicados([1,1,1,1,2,3,4,5,6]))
print(eliminar_duplicados_opti([1,1,1,1,2,3,4,5,6]))