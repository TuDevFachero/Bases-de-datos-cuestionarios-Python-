import sqlite3
import colorama
from colorama import Fore, Style
from tabulate import tabulate

conn = sqlite3.connect('datos.db')
import sqlite3

# Creamos la conexión a la base de datos
conn = sqlite3.connect('datos.db')

# Creamos la tabla para almacenar los datos



# Cerramos la conexión


nombre = input(Fore.RED + 'Ingrese su nombre: ' + Style.RESET_ALL)
edad = int(input(Fore.RED + 'Ingrese su edad: ' + Style.RESET_ALL))
email = input(Fore.RED + 'Ingrese su email electrónico: ' + Style.RESET_ALL)
telefono = input(Fore.RED + 'Ingrese su número de teléfono: ' + Style.RESET_ALL)

datos = {'Nombre': nombre, 'Edad': edad, 'email': email, 'Teléfono': telefono}

# verificar si el email electrónico incluye "@gmail.com"
if '@gmail.com' not in email:
    print(Fore.RED + 'Error: El email debe ser de gmail' + Style.RESET_ALL)
else:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO datos (nombre, edad, email, telefono) VALUES (?, ?, ?, ?)", (nombre, edad, email, telefono))
    conn.commit()
    print(Fore.GREEN + 'Datos guardados en la base de datos' + Style.RESET_ALL)
conn.close()




