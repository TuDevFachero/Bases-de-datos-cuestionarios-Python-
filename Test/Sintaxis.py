Alumnos = []

print (Alumnos)

# Agregar elementos a la lista
Alumnos.append("Juan")
print (Alumnos, "He añadido a Juan a la lista", "\n")
Alumnos.append("Pedro")
print (Alumnos, "He añadido a Pedro a la lista", "\n")
Alumnos.append("Maria")
print (Alumnos, "He añadido a Maria a la lista", "\n")
Alumnos.append("Luis")
print (Alumnos, "He añadido a Luis a la lista", "\n")
Alumnos.append("Ana")
print (Alumnos, "He añadido a Ana a la lista", "\n" )
Alumnos.append("Jose")
print (Alumnos , "He añadido a Jose a la lista", "\n")

# Eliminar elementos de la lista
Alumnos.pop(2)
print (Alumnos, "He eliminado a Maria de la lista", "\n")

# Insertar elementos en la lista
Alumnos.insert(2,"Maria")
print (Alumnos , "He insertado a Maria en la lista", "\n")

# Remover elementos de la lista
Alumnos.remove("Maria")
print (Alumnos, "He removido a Maria de la lista", "\n")

# Ordenar elementos de la lista
Alumnos.sort()
print (Alumnos, "He ordenado la lista", "\n")

# Invertir elementos de la lista
Alumnos.reverse()
print (Alumnos, "He invertido la lista", "\n")
