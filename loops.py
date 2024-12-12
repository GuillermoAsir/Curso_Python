### LOOPS ####

#While
#Este bucle hasta que no cumple X condición no se detiene.

# my_condition  =  0

# while my_condition == 12:
#     print(my_condition)
#     my_condition += 3 #Esta condicion coge como es menor que 10 le suma dos 
# else: # es opcional
#     print("Mi condición es mayor o igual a 10")

# my_condition = 0
# while my_condition < 50:
#     my_condition+=5
#     if my_condition == 51:
#         print(my_condition)
#         print("Se detiene le ejecución")
#         break 
#     print(my_condition)

# print("Fin del progama")

#Tabla del 8 
my_condition = 0
numero = int(input("Escrie un numero: "))
while my_condition < 10:
    my_condition+=1
    if my_condition == 11:
        print(my_condition)
        print("Se detiene le ejecución")
        break 
    resultado = my_condition * numero
    print(f"{my_condition }X{numero}= {resultado}")
    
