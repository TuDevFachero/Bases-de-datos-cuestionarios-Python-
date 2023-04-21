
def sumar(): #Definimos la función sumar
    x = a + b
    print (("Resultado"), (x))
def restar():#Definimos la función restar
    x = a - b
    print (("Resultado"), (x))
def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("Resultado"), (x))
def dividir():#Definimos la función dividir
    x = a / b
    print (("Resultado"), (x))
def potencia():#Definimos la función potencia
    x = a ** b
    print (("Resultado"), (x))

##########################################-2-###################################################
while True: #Creamos un bucle
    try: #Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer numero: \n")) #Solicitamos el 1er numero al usuario
        b = int(input("Ingresa el segundo numero: \n"))#Solicitamos el 2do numero al usuario
        print (("Que calculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #Preguntamos el calc
        op = str(input(""" #Ofrecemos las opciones de cálculo las cuales van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir
        5- Potencias \n"""))

##########################################-3-##################################################
        if op == '1':#Si el usuario elige opción 1 llamamos a sumar
            sumar()
            break
        elif op == '2':#Si el usuario elige opción  llamamos a restar
            restar()
            break
        elif op == '3':#Si el usuario elige opción 3 llamamos a multiplicar
            multiplicar()
            break
        elif op == '4':#Si el usuario elige opción 4 llamamos a dividir
            dividir()
            break
        elif op == '5':#Si el usuario elige opción 5 llamamos a potencia
            potencia()
            break
        else:
            print ("""Has ingresado un numero de opcion erroneo""") #En caso que el numero no
                                                                            #se encuentre
    except ZeroDivisionError:
        print ("Nuestro calculador no permite dividir por cero, intenta otro calculo!")
    except:
        print ("Error")
        op = '?'
    finally:
        print ("Gracias por utilizar nuestra calculadora")