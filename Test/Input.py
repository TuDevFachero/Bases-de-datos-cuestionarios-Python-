import colorama
from colorama import Fore, Style
from tabulate import tabulate

colorama.init()

print(Fore.BLUE + '¡Bienvenido! Por favor, responda las siguientes preguntas:' + Style.RESET_ALL)

nombre = input(Fore.GREEN + 'Ingrese su nombre: ' + Style.RESET_ALL)
edad = int(input(Fore.GREEN + 'Ingrese su edad: ' + Style.RESET_ALL))
correo = input(Fore.GREEN + 'Ingrese su correo electrónico: ' + Style.RESET_ALL)
telefono = input(Fore.GREEN + 'Ingrese su número de teléfono: ' + Style.RESET_ALL)

datos = {'Nombre': nombre, 'Edad': edad, 'Correo': correo, 'Teléfono': telefono}

# verificar si el correo electrónico incluye "@gmail.com"
if not correo.endswith("@gmail.com"):
 raise ValueError(Fore.RED + "El correo electrónico debe ser de @gmail.com" + Style.RESET_ALL)

tabla = [(k, v) for k, v in datos.items()]

print(Fore.BLUE + 'Sus datos son los siguientes:' + Style.RESET_ALL)
print(tabulate(tabla, headers=['Campo', 'Valor'], tablefmt='fancy_grid'))

