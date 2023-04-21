import sqlite3
import colorama
from colorama import Fore, Style
from tabulate import tabulate
from termcolor import colored
conn = sqlite3.connect('datos.db')

cursor = conn.cursor()
cursor.execute("SELECT * FROM datos")
registros = cursor.fetchall()
headers = [colored('id', 'red'), colored('Nombre', 'red'), colored('Email', 'red'), colored('Edad', 'red'), colored('Teléfono', 'red')]
print(tabulate(registros, headers, tablefmt='fancy_grid'))
conn.close()
