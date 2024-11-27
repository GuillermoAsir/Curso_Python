###Dict##

my_dict = dict ()
my_other_dict ={}

print(type(my_dict))
print(type(my_other_dict))

#Definir un diccionario
my_dict = {
    "nombre":"Pepe",
    "Apellido":"Perez",
    "Edad":34,
    "Lenguages": ("java","php","Phyton"),
    1:  ("java","php","Phyton")}

print(my_dict)
print(my_dict[1])
print(my_dict["Edad"])
print("Edad" in my_dict)
#~Insertar
my_dict["Calle"]= "Calle Bolnuevo"
print(my_dict)

#Actualziar
my_dict["Calle"] = "Calla Isidoro"

print(my_dict)

# Operacines cn diccioario
print("--------------------------------------------------------------")
print(my_dict.items())
print("--------------------------------------------------------------")
print(my_dict.keys())
print("--------------------------------------------------------------")
print(my_dict.values)

#Eliminar una clave

del my_dict["Calle"]
print(my_dict)

my_list = ["Nombre", 1, "Apellido"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(["Nombre", 1, "Apellido"])
#Input

# #Output
# input1 =input()
# print(input1)
print("---------------------------------------------------------")
print("Dame numero")
num1 =int(input1)
print("Dame un número no letras")
print =int(input())