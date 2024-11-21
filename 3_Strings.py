### String ###

#Declaración de string usando comillas simples y dobles
my_string ="Hola uno"
my_other = 'Hola dos'

print(my_string, my_other)
print(my_string)
print(my_other)

#Concatenar string con un espacio en blanco
print(my_string+" "+ my_other)

#Crear un salo de línea

variable3 = "Esto es un string\ncon salto de linea"
print(variable3)

# Insertar tabulación

variable4 = "\tEsto es im string con salto de linea"
print(variable4)

# Escapar "ver" caracteres especiales
variable5= "\\tEsto es im string con salto de linea"
print(variable5)

# Formato de stirngs

name, surname, age ="Guillermo", "Cañavate ",37

print(name, surname, age)
print("mi nombre es {} {} y mi edad es {}".format(name,surname,age))

#Formateo antiguo usando %
print("mi nombre es %s %s y mi edad es %d" % (name,surname,age))

# Concatenar varios string (str convierte en la variable age en string)

print("Mi nombre"+ name +" "+ surname +"y mi edad es "+ str(age))

# Formateo usando f-strings (moderno)

print(f"mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquentado caracteres
lenguage = "python"
a,b,c,d,e,f =lenguage

print(a)
print(b)

# DIvidir string (Slice)

language_slice = lenguage[1:3]
language_slice = lenguage[-2] #Toma  el segundo caracter por detras

language_slice = lenguage[0:6:2] # Lo coge todos del 0 al 6 y luego va saltando de dos en dos
# Reveritr la cadena
language_slice = lenguage[::-1]
print(language_slice)

#### Funciones de string ### 

#Remplazar caracteres de un string
fruit = "Stramberry"

fruit_replace= fruit.replace('r', 'R')
print(fruit_replace)

#Convierte la primera letra en mayuscula
print(fruit.capitalize())

#Convertir todo el texto en Mayusculas
print(fruit.upper())

#Convertir en minusucla
print(fruit.lower())

#Verificar que esta todo en minuscula
print(fruit.islower())

#contar cuantos caracteres hay del mismo tipo 
print(fruit.count("t")) 

#contar todos los caracteres de una palabra

variable1 =print(len(fruit))

print (f"la variable (fruit) tiene: "+ str(len(fruit)))

numero_de_letras = len(fruit)
print(numero_de_letras)
print(str(numero_de_letras).isnumeric())

#Verificar si comienza la cadena con unos caracteres
#Ejemplo Py
print(lenguage.startswith("py"))



#age= int(input("CUal es tu edad?: "))
# if age = >18: 
#  print ("eres menos de edad ")
#    else age = <18:
#    print("Eres mayor de edad")


