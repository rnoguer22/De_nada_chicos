# Clase de programacion 16/11/2021


# ------------------------------------------------------


# CADENAS DE CARACTERES

cadena = "TesT" 
cadena_minuscula = cadena.lower() 
print(cadena) 
print(cadena_minuscula) 

cadena_mayusculas = cadena.upper() 
print (cadena)
print (cadena_mayusculas)

print (len(cadena))

cadena = 'abcdaefabcefab' 
print (cadena.count ('a'))  # Devuelve 4 

cadena = 'abcdaefabcefab' 
print (cadena.count('ab'))  # Devuelve 3 

cadena = 'abcdaefabcefab' 
print (cadena.count('abc'))  # Devuelve 2 

posicion = cadena.index("a") # La primera posición de un carácter en una cadena es siempre 0 y la última n - 1, n es la longitud de la cadena
print (posicion)

posicion2 = cadena.index("a", posicion + 1) 
print (posicion2)

posicion3 = cadena.index("a", posicion2 + 1)
print (posicion3)

def posiciones(cadena, fragmento) : 
    posicion = -1 
    for i in range(cadena.count(fragmento)): 
        posicion = cadena.index ("a", posicion + 1) 
        print("Posición n°{}:{}".format( i + 1, posicion)) 

print (cadena.replace("a", "A")) # Devuelve 'AbcdAefAbcefAb'

print (cadena.replace("ab", "AB")) # Devuelve 'ABcdaefABcefAB' 

print (len(cadena.replace("abc", "[--O--]"))) # Devuelve '[--O--]daef[--O--]efab'
# No tiene por que tener la misma longitud que "cadena"

print (cadena[0]) # Vemos que es posible acceder a un carácter concreto de una cadena mediante el operador corchete

import unicodedata # Convierte las cadenas de texto en unicode
unicodedata.category('a')  # Devuelve 'Ll' 
unicodedata.category('A')  # Devuelve 'Lu' 
unicodedata.category('é')  # Devuelve 'Ll' 
unicodedata.category('É')  # Devuelve 'Lu' 
unicodedata.category('ç')  # Devuelve 'Ll' 
unicodedata.category('ñ')  # Devuelve 'Ll' 
unicodedata.category(chr(0x10880))  # Devuelve 'Cn' 
unicodedata.category('>')  # Devuelve 'Sm' 

import string # Este módulo contiene algunas cadenas que contienen todos los caracteres de un tipo particular
string.ascii_letters 
# Devuelve 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
string.ascii_lowercase 
# Devuelve 'abcdefghijklmnopqrstuvwxyz' 
string.ascii_uppercase 
# Devuelve 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

string.digits # Así como las cifras (según la base)
# Devuelve '0123456789' 
string.hexdigits 
# Devuelve '0123456789abcdefABCDEF' 
string.octdigits 
# Devuelve '01234567' 

string.punctuation # Los signos de puntuación y los espacios:
# Devuelve '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 
string.whitespace 
# Devuelve ' \t\n\r\x0b\x0c'

palabras = cadena.split() # He aquí cómo dividir una cadena de caracteres

"<pegamento>".join(palabras)

lista_caracteres = list(cadena) # Es posible dividir carácter por carácter una cadena de caracteres muy fácilmente
# Se obtiene así una lista, igual que si hubiéramos utilizado el método split y lo que hemos detallado hasta el momento


# ------------------------------------------------------


# LISTAS

lista = list("Python is awesome") 
# Lo que equivale a declarar la lista así:

lista =  ['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'a', 
'w', 'e', 's', 'o', 'm', 'e']

print (lista[4]) # Podemos usar las listas para recuperar un elemento

print (lista[-3]) # También cómo utilizar un índice negativo para partir del final

print (lista[:6]) # = ['P', 'y', 't', 'h', 'o', 'n'] # Extraccion de una lista

print (lista[7:9]) # =  ['i', 's'] # También es posible extraer los caracteres séptimo y octavo
#  siempre van del primero incluido al último excluido

print (lista[10:]) # =  ['a', 'w', 'e', 's', 'o', 'm', 'e'] # Para ir hasta el final, podemos dejar el segundo argumento vacío

print (lista[2::5]) # =  ['t', 'i', 'e']

print (lista[11]) # = "b" # El índice también permite asignar un nuevo valor a esta ubicación de la lista

del (lista[15]) # Eliminar un elemento de una lista

del lista[:7] # Eliminar varios elementos de una lista a la vez

# lista.remove("t") # También es posible eliminar un elemento particular de la lista (sin saber su índice)

while " " in lista: 
   lista.remove(" ") # De esta manera eliminamos todos los elementos de una lista

print (lista.pop()) # Por último, es posible utilizar la lista como una pila eliminando un valor al final y devolviéndolo

print (lista.append("h")) # O agregando un valor al final

print (lista.insert(2, "d")) # También podemos agregar valores en cualquier lugar, basta con precisar el índice de inserción y el valor que se desee insertar

print (lista.extend(["i", "j"])) # Por último, podemos agregar otra lista, al final


# ------------------------------------------------------


# DICCIONARIOS

agenda = { 
    "Climent": "601020304", 
    "Claudia": "934123456", 
    "Mateo": "917101345", 
} 

print (agenda["Claudia"])

agenda["Sebastián"] = "791827364" # Agregamos un nuevo valor al diccionario
# Si la clave existe, entonces su valor se actualiza; en caso contrario, se crea un nuevo registro

for nombre, telefono in agenda.items(): # He aqui la forma de recorrer un diccionario
    print("El número de {} es {}".format(nombre, telefono))

# Y si realmente es necesario recorrer el diccionario en orden, 
# tendremos que iterar sobre las claves, pero con la precaución de ordenarlas previamente
for nombre in sorted(agenda.keys()): 
    print("El número de {} es {}".format(nombre, agenda[nombre])) 

print (agenda.get("Casiopea")) # Y accedemos a una entrada del diccionario, incluso aunque no estemos seguros de que exista

print (agenda.get("Casiopea", "987654321")) # Y pedirle que devuelva un valor por defecto si no existe la clave