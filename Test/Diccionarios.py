from tabulate import tabulate
from termcolor import colored

# Definir los diccionarios
Diccionario1 = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 25,
    "Cursos": ["Python", "Django", "JavaScript"],
    "Estudios": ["Primaria", "Secundaria", "Universidad"],
    "Sueldo": "2774.45€",
    "Hijos": None,
    "Pais": "Mexico",
    "Estado": "CDMX",
    "Ciudad": "CDMX",
    "Direccion": "Av. Siempre Viva 1h23",
    "CodigoPostal": "12345",
    "Telefono": "1234567890",
    "Email": "juan@gmail.com",
    "Activo": True
}

Diccionario2 = {
    "Nombre": "Pedro",
    "Apellido": "Gomez",
    "Edad": 30,
    "Cursos": ["Python", "Django", "JavaScript"],
    "Estudios": ["Primaria", "Secundaria", "Universidad"],
    "Sueldo": "1353.50€",
    "Hijos": None,
    "Pais": "España",
    "Estado": "Madrid",
    "Ciudad": "Madrid",
    "Direccion": "Calle 123",
    "CodigoPostal": "12345",
    "Telefono": "1234567890",
    "Email": "pedrogmz@gmail.com",
    "Activo": True
}

Diccionario3 = {
    "Nombre": "Maria",
    "Apellido": "Gomez",
    "Edad": 36,
    "Cursos": ["Python", "Django"],
    "Estudios": ["Primaria", "Secundaria", "Universidad", "Maestria"],
    "Sueldo": "5000.50€",
    "Hijos": None,
    "Pais": "España",
    "Estado": "Madrid",
    "Ciudad": "Madrid",
    "Direccion": "Calle 123",
    "CodigoPostal": "12345",
    "Telefono": "1234567890",
    "Email": "adkf@gmail.com",
    "Activo": True
}

from termcolor import colored
from tabulate import tabulate

headers = [colored("Nombre", "green"), colored("Apellido", "green"), colored("Edad", "green"), colored("Cursos", "green"),
           colored("Estudios", "green"), colored("Sueldo", "green"), colored("Hijos", "green"), colored("Pais", "green"),
           colored("Estado", "green"), colored("Ciudad", "green"), colored("Direccion", "green"), colored("Codigo Postal", "green"),
           colored("Telefono", "green"), colored("Email", "green"), colored("Activo", "green")]

data1 = [Diccionario1["Nombre"], Diccionario1["Apellido"], Diccionario1["Edad"], ", ".join(Diccionario1["Cursos"]), ", ".join(Diccionario1["Estudios"]),
         colored(str(Diccionario1["Sueldo"]), "red" if Diccionario1["Sueldo"] < "1500€" else "green"), Diccionario1["Hijos"], Diccionario1["Pais"], Diccionario1["Estado"], Diccionario1["Ciudad"],
         Diccionario1["Direccion"], Diccionario1["CodigoPostal"], Diccionario1["Telefono"], Diccionario1["Email"], Diccionario1["Activo"]]

data2 = [Diccionario2["Nombre"], Diccionario2["Apellido"], Diccionario2["Edad"], ", ".join(Diccionario2["Cursos"]), ", ".join(Diccionario2["Estudios"]),
         colored(str(Diccionario2["Sueldo"]), "red" if Diccionario2["Sueldo"] < "1500€" else "green"), Diccionario2["Hijos"], Diccionario2["Pais"], Diccionario2["Estado"], Diccionario2["Ciudad"],
         Diccionario2["Direccion"], Diccionario2["CodigoPostal"], Diccionario2["Telefono"], Diccionario2["Email"], Diccionario2["Activo"]]

data3 = [Diccionario3["Nombre"], Diccionario3["Apellido"], Diccionario3["Edad"], ", ".join(Diccionario3["Cursos"]), ", ".join(Diccionario3["Estudios"]),
         colored(str(Diccionario3["Sueldo"]), "red" if Diccionario3["Sueldo"] < "1500€" else "green"), Diccionario3["Hijos"], Diccionario3["Pais"], Diccionario3["Estado"], Diccionario3["Ciudad"],
         Diccionario3["Direccion"], Diccionario3["CodigoPostal"], Diccionario3["Telefono"], Diccionario3["Email"], Diccionario3["Activo"]]

table = [data1, data2, data3]

print(tabulate(table, headers, tablefmt="fancy_grid"))

