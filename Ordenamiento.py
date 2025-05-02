print(" \n****Bienvenidos****" \
"\n " \
"\nOrdenamiento por burbuja")
def ordenamiento_burbuja(lista):
    n = len(lista)
    tope = n
    while tope > 1:
        for indice in range(tope):
            if indice + 1 < tope:
                if lista[indice] > lista[indice + 1]:
                    lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
        tope -= 1

if __name__ == "__main__":
    lista_numeros = [4, 3, 2, 1, 5, 10, 9]
    print("Lista original:", lista_numeros)
    ordenamiento_burbuja(lista_numeros)
    print("Lista ordenada:", lista_numeros)
print(" ")

# Ordenamiento I
print("Ordenamiento por insercion")
def ordenamiento_por_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]  
        j = i - 1  
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]  
            j -= 1  
        lista[j + 1] = clave

if __name__ == "__main__":
    lista_numeros = [6, 3, 5, 2, 8, 19, 7]
    print("Lista original:", lista_numeros)
    ordenamiento_por_insercion(lista_numeros)
    print("Lista ordenada:", lista_numeros)