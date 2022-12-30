def seleccionOrden(lista,largoLista,contador):
    if contador<largoLista:
        pequeño=lista[contador]
        posicion=contador
        for i in range(contador+1,largoLista):
            if lista[i]<pequeño:
                pequeño=lista[i]
                posicion=i
        lista[contador],lista[posicion]=lista[posicion],lista[contador]
        seleccionOrden(lista,largoLista,contador+1)
A=[3,6,9,12,4,5,23,9,1]
seleccionOrden(A,len(A),0)
print(A)