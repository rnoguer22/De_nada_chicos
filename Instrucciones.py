# INSTRUCCIONES 


# -------------------------------------------------


# Funcion dentro de otra funcion
def print_add(a, b): 
    def add(a, b): 
            return a+b 
    print(add(a, b))   
print_add(5, 6)


print ( "------------------------------------------------" )

"FUNCIONES LAMBDA"
 
# Las funciones lambda son una forma de escribir una función anónima que utiliza una sintaxis 
# análoga a la que se conoce en matemáticas:
print (lambda x: x**2)

print (list(map(lambda x: x**2, range(10)))) 

# Si bien las funciones lambda se utilizan con el objetivo de crear funciones anónimas, 
# es posible darles un nombre:
f = lambda x: x**2 
print (f(5)) 
# 25 
print (list( map(f, range(10))))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = lambda x, y: x*y**2 
print (g(4, 2)) 
# 16

"Como conclusión podemos decir que la filosofía de una función lambda es describir una relación"
"entre parámetros y una expresión que los utiliza, de forma algebraica." 


print ( "------------------------------------------------" )

"CLASE"

class MiClase: 
     atributo = 42 
     def metodo(self): 
         pass


# print ( "------------------------------------------------" )

"INSTRUCCION VACIA"

def f():  # Funcion vacia
     pass

class A:  # Clase vacia
     pass

"Esta instrucción permite marcar la presencia de un bloque indentado,"
"con el objetivo de respetar las reglas de gramática relativas a los bloques aunque" 
"no se realice ninguna acción dentro de dicho bloque."


# print ( "------------------------------------------------" )

"BORRADO"

a=5 
del a
# print (a) 
"Esto pot lo tanto da lugar a un error:"
#Traceback (most recent call last): 
  #File "<stdin>", line 1, in <module> 
#NameError: name 'a' is not defined

b=list(range(10))  
del b[5]   #Borramos un índice  
del b[2:7:2]   #Borramos una franja  
print (b)  
# [0, 1, 3, 6, 8, 9]

c={'a': 'A', 'b': 'B', 'c': 'C'}  
del c['b']   # clave  
print (c)  
# {'a': 'A', 'c': 'C' }


print ( "------------------------------------------------" )

"DEVOLVER EL RESULTADO DE UNA FUNCION"

def f():  
     pass  
print(f())  
# None 

def uno():
    return 1
print (uno())
# 1

def f(): 
     return 1, 2, 3
print (f())
print (type(f()))
# En realidad, se devuelve un único valor, y se trata de una n-tupla. 
# En efecto, escribir return 1, 2, 3 equivale exactamente a escribir return (1, 2, 3), 
# la coma es el separador característico de una n-tupla.


print ( "------------------------------------------------" )


"INSTRUCCIONES CONDICIONALES"

def evaluacion(num): 
     r = 'positivo' 
     if num < 0: 
         r = 'negativo' 
     return r 
print (evaluacion(3))


print ( "------------------------------------------------" )


"INSTRUCCION ELIF"

if False:  
    print(1)  
elif True:  
    print(2)  
elif True:  
    print(3)  # Esta instruccion no se ejecuta porque cuando un elif se cumple,
              # no se ejecutan los demas que estan por debajo


print ( "------------------------------------------------" )

"INSTRUCCION ELSE"
  
def f(condición):  
     if condición:  
         print(True)  
     else:  
         print(False)  
   
def evaluación(num):  
     if num < 0:  
         r = 'negativo'  
     else:  
         r = 'positivo'  
     return r 

print (f(2 == 2))
print (evaluacion)


print ( "------------------------------------------------" )

"PROFUNDIZANDO EN LAS CONDICIONES"

a = (2, 3, 5, 7, 11, 13)
a in (2, 3, 5, 7, 11, 13) 
# True 
print (a == 2 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13) 
# True


# print ( "------------------------------------------------" )

"INSTRUCCION CONTINUE"

def positivo(l):  
     for a in l:  
         if a < 0:  
             continue  # Pasaria a la siguiente instruccion
         print(a)


print ( "------------------------------------------------" )

"INSTRUCCION ELSE EN UN BUCLE"

def es_valido(l): 
     for a in l: 
         if a < 0 or a > 20: 
             return False  
     else:  # La funcion "else" tambien es usualmente asociada a bucles for
             return True

for n in range(2,10): 
     x = 2 
     while x <= n**(1/2): 
         if n % x == 0: 
             print('%i vale %i * %i' % (n, x, n/x)) 
             break 
         x += 1 
     else:  # Pasa los mismo para un bucle while
         print('%i es un número primo' % n) 
     n += 1