import linked_list

lista = linked_list.List()

lista.append(5)        
lista.append(7)
lista.append(9)
lista.append(1)
lista.append(12)

print("Lista original:")
print(lista)
print("El tamaño de la lista es", lista.size(), "\n")

lista.delete(0)
lista.delete(3)

print("La lista con los elementos en 0 y 3 eliminados:")
print(lista)
print("El tamaño de la lista es", lista.size(), "\n")

pos = lista.getElement(0)

lista.replace(0, 2)

print("La lista con el elemento en la posición 0 siendo reemplazado por 2:")
print(lista, "\n")

lista_clonada = lista.clone()

lista_clonada.interchangeFirstOnes()

print("La lista clonada e intercambiada en los primeros es:")
print(lista_clonada)

lista.expand(lista_clonada)

cantidad = lista.ocurrenceOf(9)
