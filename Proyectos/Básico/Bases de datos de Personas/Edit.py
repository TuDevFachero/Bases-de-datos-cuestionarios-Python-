import sqlite3
import colorama
from colorama import Fore, Style
from tabulate import tabulate
conn = sqlite3.connect('datos.db')
p = input(Fore.MAGENTA + 'Qué desea editar?\n ' + Fore.YELLOW + 'Opciones:' + '\n' + Fore.CYAN + '1- ID' + '\n' + '2- Nombre' + '\n' + '3- Edad\n' + '4- Email\n' + '5- Teléfono\n' + '6- Ver base de datos\n' + Fore.RED + 'Respuesta: ' + Style.RESET_ALL)
def id ():
    p = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
    id = input(Fore.RED + 'Cual es el nuevo ID? ' + Style.RESET_ALL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
    registro = cursor.fetchone()
    if registro is None:
        print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
    else:
        cursor.excecutte("UPDATE datos SET id = ? WHERE id = ?", (id,))
        conn.commit()
        print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
def nombre ():
    p = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
    nombre = input(Fore.RED + 'Cual es el nuevo nombre? ' + Style.RESET_ALL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
    registro = cursor.fetchone()
    if registro is None:
        print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
    else:
        cursor.excecutte("UPDATE datos SET nombre = ? WHERE id = ?", (nombre,))
        conn.commit()
        print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
def edad ():
    p = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
    edad = input(Fore.RED + 'Cual es la nueva edad? ' + Style.RESET_ALL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
    registro = cursor.fetchone()
    if registro is None:
        print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
    else:
        cursor.excecutte("UPDATE datos SET edad = ? WHERE id = ?", (edad,))
        conn.commit()
        print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
def email ():
    p = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
    email = input(Fore.RED + 'Cual es el nuevo email? ' + Style.RESET_ALL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
    registro = cursor.fetchone()
    if registro is None:
        print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
    else:
        cursor.excecutte("UPDATE datos SET email = ? WHERE id = ?", (email,))
        conn.commit()
        print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
def telefono ():
    p = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
    telefono = input(Fore.RED + 'Cual es el nuevo teléfono? ' + Style.RESET_ALL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
    registro = cursor.fetchone()
    if registro is None:
        print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
    else:
        cursor.excecutte("UPDATE datos SET telefono = ? WHERE id = ?", (telefono,))
        conn.commit()
        print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)


if p == '1':
    id()
elif p == '2':
    nombre()
elif p == '3':
    edad()
elif p == '4':
    email()
elif p == '5':
    telefono()
elif p == '6':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datos")
        registros = cursor.fetchall()
        print(tabulate(registros, headers=['ID', 'Nombre', 'Edad', 'Email', 'Teléfono'], tablefmt='fancy_grid'))
        input(Fore.MAGENTA + '\nPresione cualquier tecla para continuar...' + Style.RESET_ALL)
        print(Fore.GREEN + 'Bienvenido al menú principal' + Style.RESET_ALL)
        print(Fore.MAGENTA + 'Qué desea editar?\n ' + Fore.YELLOW + 'Opciones:' + '\n' + Fore.CYAN + '1- ID' + '\n' + '2- Nombre' + '\n' + '3- Edad\n' + '4- Email\n' + '5- Teléfono\n' + '6- Ver base de datos\n' + Fore.RED + 'Respuesta: ' + Style.RESET_ALL)    
else:
        print(Fore.RED + 'Error: No existe un registro con esa información' + Style.RESET_ALL)


conn.close()
   
   