from colorama import Fore, Style
from tabulate import tabulate
import sqlite3
import colorama

conn = sqlite3.connect('datos.db')

print(Fore.MAGENTA + 'Bienvenido a la base de datos' + Style.RESET_ALL)
print(Fore.RED + '¿Qué desea hacer?' + Style.RESET_ALL)
print(Fore.YELLOW + '|----------------------|' + Fore.CYAN + ' Lista de opciones ' + Fore.YELLOW + '|----------------------|' + Style.RESET_ALL)
print(Fore.BLUE + '''
-1- Agregar un registro
-2- Editar un registro
-3- Eliminar un registro
-4- Ver la base de datos
-5- Salir
''')
re = input(Fore.RED + 'Respuesta: ' + Style.RESET_ALL)
sys = True
def agregar ():
    id = input(Fore.RED + 'ID: ' + Style.RESET_ALL)
    nombre = input(Fore.RED + 'Nombre: ' + Style.RESET_ALL)
    edad = input(Fore.RED + 'Edad: ' + Style.RESET_ALL)
    email = input(Fore.RED + 'Email: ' + Style.RESET_ALL)
    telefono = input(Fore.RED + 'Teléfono: ' + Style.RESET_ALL)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO datos VALUES (?, ?, ?, ?, ?)", (id, nombre, edad, email, telefono))
    conn.commit()
    print(Fore.GREEN + 'Registro agregado a la base de datos' + Style.RESET_ALL)

def editar ():
    print(Fore.MAGENTA + 'Qué desea editar?\n ' + Fore.YELLOW + 'Opciones:' + '\n' + Fore.CYAN + '1- ID' + '\n' + '2- Nombre' + '\n' + '3- Edad\n' + '4- Email\n' + '5- Teléfono\n' + '6- Ver base de datos\n' + Fore.RED + 'Respuesta: ' + Style.RESET_ALL)
    p = input(Fore.RED + 'Respuesta: ' + Style.RESET_ALL)
    if p == '1':
        id = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
        id = input(Fore.RED + 'Cual es el nuevo ID? ' + Style.RESET_ALL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
        registro = cursor.fetchone()
        if registro is None:
            print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
        else:
            cursor.execute("UPDATE datos SET id = ? WHERE id = ?", (id,))
            conn.commit()
            print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
    elif p == '2':
        id = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
        nombre = input(Fore.RED + 'Cual es el nuevo nombre? ' + Style.RESET_ALL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
        registro = cursor.fetchone()
        if registro is None:
            print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
        else:
            cursor.execute("UPDATE datos SET nombre = ? WHERE id = ?", (nombre,))
            conn.commit()
            print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
    elif p == '3':
        id = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
        edad = input(Fore.RED + 'Cual es la nueva edad? ' + Style.RESET_ALL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
        registro = cursor.fetchone()
        if registro is None:
            print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
        else:
            cursor.execute("UPDATE datos SET edad = ? WHERE id = ?", (edad,))
            conn.commit()
            print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
    elif p == '4':
        id = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
        email = input(Fore.RED + 'Cual es el nuevo email? ' + Style.RESET_ALL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
        registro = cursor.fetchone()
        if registro is None:
            print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
        else:
            cursor.execute("UPDATE datos SET email = ? WHERE id = ?", (email,))
            conn.commit()
            print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
    elif p == '5':
        id = input(Fore.RED + 'Ingrese el ID del registro que desea editar: ' + Style.RESET_ALL)
        telefono = input(Fore.RED + 'Cual es el nuevo teléfono? ' + Style.RESET_ALL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
        registro = cursor.fetchone()
        if registro is None:
            print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
        else:
            cursor.execute("UPDATE datos SET telefono = ? WHERE id = ?", (telefono,))
            conn.commit()
            print(Fore.GREEN + 'Registro editado de la base de datos' + Style.RESET_ALL)
    elif p == '6':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datos")
        print(tabulate(cursor.fetchall(), headers=['ID', 'Nombre', 'Edad', 'Email', 'Teléfono'], tablefmt='psql'))
    else:
        print(Fore.RED + 'Error: Opción no válida' + Style.RESET_ALL)

def eliminar ():
    id = input(Fore.RED + 'Ingrese el ID del registro que desea eliminar: ' + Style.RESET_ALL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
    registro = cursor.fetchone()
    if registro is None:
        print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
    else:
        cursor.execute("DELETE FROM datos WHERE id = ?", (id,))
        conn.commit()
        print(Fore.GREEN + 'Registro eliminado de la base de datos' + Style.RESET_ALL)
    
def ver ():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos")
    print(tabulate(cursor.fetchall(), headers=['ID', 'Nombre', 'Edad', 'Email', 'Teléfono'], tablefmt='fancy_grid'))

def salir ():
    print(Fore.GREEN + 'Gracias por usar el programa' + Style.RESET_ALL)
    exit()

if re == '1':
    agregar()
elif re == '2':
    editar()
elif re == '3':
    eliminar()
elif re == '4':
    ver()
elif re == '5':
    salir()
else:
    print(Fore.RED + 'Error: Opción no válida' + Style.RESET_ALL)


