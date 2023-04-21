import sqlite3
import colorama
from colorama import Fore, Style
from tabulate import tabulate
conn = sqlite3.connect('datos.db')
id = input('Ingrese el ID del registro que desea eliminar: ')

cursor = conn.cursor()
cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))
registro = cursor.fetchone()

if registro is None:
    print(Fore.RED + 'Error: No existe un registro con ese ID' + Style.RESET_ALL)
else:
    cursor.execute("DELETE FROM datos WHERE id = ?", (id,))
    conn.commit()
    print(Fore.GREEN + 'Registro eliminado de la base de datos' + Style.RESET_ALL)

conn.close()