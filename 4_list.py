### list ###
#Defición de listas vacías

my_list =list() # Crear una lista vacia usando el constructor list()
my_other_list = [] # Imprime una lista vacia usando []

print(len(my_list)) # Imprime la lomgitud de la lsita , en este caso 0
print(len(my_other_list)) # Imprime la logitud de la lista, este caso 0

#Defenir una lista con valores

my_list =[35,20,40,35,14]

print(my_list)
print(len(my_list))

# Lista de tipos diferentes 
my_type_list = ("Hola", 3, "Mundo", 56, 1.88, )
print(my_type_list)
print(len(my_type_list))

#Avveso de un elemento de una lista
print(my_type_list[0]) # Accede al primer elemento
print(my_type_list[-1]) # Accede al último elemento
print(my_type_list[-4]) # Accede el primer elemento
print(my_type_list.count(3)) # Cuenta el numero de elementos que se repiten el numero 3

#Como buscar el indice termino HOla el my_type_list = ["Hola", 3, "Mundo", 56, 1.88,]

print (my_type_list.index("Hola")) #Cuenta el número de palabras que hay en la lista contando desde 0
print (my_type_list.index("Mundo")) #Cuenta el número de palabras que hay en la lista sale uno por si esta la palabra "Mundo"

#Desempaquetar una lista 

#var1, var2, var3, var4, var5 = my_type_list #Para desempaquetar tienen que tener la misma cantidad de la lista

#print(var1, var2, var3,)

var1,var2 = my_type_list[0], my_type_list[3]

print(var1 ,var2)

#Concatenar lista

list1 = ["Hola", 3, "Mundo" ]
list2 = ["Hola", 3, "Mundo", 56, 1.88, ]



list3 =list1 + list2

#Curl de elementos (creación, inserción, actualizadación y eliminación)
#mirar append que no me va

list3.append("Jorge")
print (list3)

list3.insert(3,"Jorge")
print (list3)
list3.remove("Hola")
print (list3)
list3[0]="Javier"
print (list3)

resultado= list3.pop() #
print(list3)
print(resultado)

resultado= list3.pop(0) #Para borrar a Javier porque esta en 0 con lis3[0]"Javier"
print(resultado)
del list3[1]
print(list3)

#Hacer una copia de una lista
list4 = list3.copy()
print(list4)

list3.clear() #Borramos el contenido de la lista
print(list3)
print(list4)

list4.reverse()
print(list4)

#list4.sort() #No se puede ordenar diferentes tipos

list_int = [45,44,56,1]
list_int.sort(reverse=True)
print(list_int)

lista_string ="Hola NOS VAMOS A TOMAR ...."
print (lista_string)
print(type(lista_string))