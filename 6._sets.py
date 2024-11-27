##Sets: es una coleccion de elementos unicos y desordenados.
#Formas de declarar sets
my_sets = set()
my_other_sets ={} # Es un sets vacio, phyton lo declara como diccionario

print(type(my_sets))
print(type(my_other_sets))

#Como se declara con elementos
var1 = {"Hola", "Jose", 34}
print(type(var1))

var1.add("Hola")
print(var1)

#eliminar un elemento 
var1.remove("Hola")
print(var1)

#Busqueda de elemento en el set (conjunto)
print("Jose" in var1) #Si existe el elemento.

# Transformacion de set en lista
var3= list(var1)
print(type(var3))
print(var3)

#UNION
my_other_set = {"Javier", "Aaran", "KK"}
my_other_languages = {"php", "Css"}

var_unio = my_other_set.union(my_other_languages).union({"java","C#" "C++"})  #Unir de forma ordenada
print(var_unio)
#Diferencia

my_other_languages ={"java","C#"}

print (my_other_languages.difference(var_unio))

#Muestra la diferencia
print(var_unio.difference(my_other_languages))

