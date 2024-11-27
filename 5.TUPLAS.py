#tuplas

#Dos formas de declarar una tupla
my_tuple =tuple ()
my_other_tuple = ()

my_tuple ="holas"
my_tuple = 3
#Las cajas se convierte en el tipo que le pongamos si es int(numero) etc..
var1 =(34,45,45)
var2 = (34,45,45,"hola","mundo")


print(var1)
print(var2)
print(my_tuple)

#Acceso de información de la tupla
#       0   1  2 (los valores)
#var1 =(34,45,45)
print(var1[0]) # Acceso  primer valor
print(var1[-1]) # Acceso  al últmo de la tupla (contamos desde -1, -2 -3)
#print(var1[4]) # Acceso  al cuarto valor  (no existe) (fuera de rango)
# print(var1[-6]) # Acceso al sexto valor de al revers (fuera de rango)
#Control + K + C comenta control +k + u DESCOMENTA

var3 = ("Hola" , "Jose")
var4 = (":", "Dime tu edad")

var5 = var3 + var4
print(var5)

#Dividr tuplas
#var5 lo que muestra es ('Hola', 'Jose', ':', 'Dime tu edad')
var6 = var5[0:2] #ver el contenido del var 3
print(var6)

#tu no sabes las posiciones, como se puede saber

print(var5.index("Hola"))
print(var5.index("Jose"))

#Contar veces que se repite  una valor en una tupla
print(var5.count("Jose"))

#Cargarte una tupla
var5 =list(var5)
print(type(var5))
print(var5)
#Aparece entre corchetes porque ahora no es una tupla, es una lita.
#transformar en una lista en un tupla
var5=tuple(var5)
print(type(var5))
print(var5)
#Vuelve los parentesis porque ahora es una tupla
