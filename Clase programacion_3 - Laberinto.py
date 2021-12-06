# CLASE DE PROGRAMACION 26/11/2021



# ------------------------------------------------------


class Punto():  # """Representa un punto en el espacio""" 
 
    def __init__(self, x, y, z): 
        """Método de inicialización de un punto en el espacio""" 
        self.x = x 
        self.y = y 
        self.z = z 
 
    def mostrar(self): 
        """Método temporal utilizado para mostrar nuestro punto""" 
        print("Punto ({}, {}, {})".format(self.x, self.y, self.z)) 

# He aquí ahora cómo crear un punto y mostrarlo:
p = Punto(1, 2, 3) 
p.mostrar()

# Ejercicio: Cree un método que permita calcular el módulo del punto (distancia respecto al origen).

# Ejercicio: Cree un método que permita calcular la distancia de un punto en curso respecto a otro.

# Ejercicio: Cree un método que permita calcular la distancia del punto en curso respecto al origen (es decir, el módulo).

# Si desea una pista para empezar, he aquí el esqueleto de esta clase:

class Punto: 
    """Representa el punto en el espacio""" 
 
    def __init__(self, x, y, z): 
        """Método de inicialización de un punto en el espacio""" 
        self.x = x 
        self.y = y 
        self.z = z 
 
    def mostrar(self): 
        """Método temporal utilizado para mostrar nuestro punto""" 
        print("Punto ({}, {}, {})".format(self.x, self.y, self.z)) 
 
    def modulo(self): 
        """Devuelve el módulo del punto"""
        modulo_punto = ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
        return modulo_punto
 
    def distancia(self, other): 
        """ 
        Devuelve la distancia respecto a otro punto 
        Las variables self y other son, ambas, puntos. 
        """ 
        distancia_dos_puntos = ((self.x - other.x)**2 + (self.x -  other.x)**2 + (self.x - other.x)**2)**(1/2)
        return distancia_dos_puntos

    def distancia_y_modulo(self, other=None): 
        """Devuelve la distancia respecto a otro punto o por  
        defecto al origen""" 
        if other == None:
            other = Punto (0,0,0)
        return other
    
    def __add__(self, other): 
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    
    def __sub__(self, other): 
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    
    def __mul__(self, other): 
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __str__(self, other):
        return print (str(self, other))

# He aquí también la manera de inicializar esta clase y utilizar las funciones:

p = Punto(1, 2, 3) 
p.mostrar() 
print("|p| =", p.modulo()) 
print("la distancia entre p y (1, 2, 5) es ", p.distancia(Punto(1, 2, 5))) 
print("|p| = ", p.distancia_y_modulo(other=p)) 
print("la distancia entre p y (1, 2, 5) es ", 
p.distancia_y_modulo(Punto(1, 2, 5))) 

# La solución está en el archivo Guía/24_Clases/24__02__Ejercicio_1.py.


# ------------------------------------------------------


class Punto2D(Punto): 
    """Representa un punto en el plano"""
    def __init__(self, x, y): 
        """Método de inicialización de un punto en el plano""" 
        super().__init__(x, y, 0)   # El super es
    
    def __str__(self): 
        return "Punto2D ({self.x}, {self.y})".format(self=self) 

p = Punto2D(1, 2) 
p += Punto2D(3, 0)
print (p)


class MostrableMixin: 
 
    str_format = "PrettyPrintableObject" # Este str_format viene de nuestra clase madre
 
    def __str__(self): 
        """ 
        Representación automática de un objeto, 
        basada en el uso de una cadena de formateo 
        que es un atributo de la clase 
        """ 
        return self.str_format.format(self=self)


class NombreAutomaticoMixin: 
 
    ordinal = 65 
 
    def __init__(self): 
        self.letra = chr(NombreAutomaticoMixin.ordinal) 
        NombreAutomaticoMixin.ordinal += 1


class Punto(MostrableMixin, NombreAutomaticoMixin): 
    """Representa un punto en el espacio""" 
 
    str_format = "Punto {self.letra} ({self.x}, {self.y}, {self.z})" 
 
    def __init__(self, x, y, z): 
        """Método de inicialización de un punto en el espacio""" 
        super().__init__() 
        self.x, self.y, self.z = x, y, z 
 
    # [ ... código omitido ... ]


class Punto2D(Punto): 
    """Representa un punto en el plano""" 
 
    str_format = "Punto2D {self.letra} ({self.x}, {self.y})" 
 
    def __init__(self, x, y): 
        """Método de inicialización de un punto en el plano""" 
        super().__init__(x, y, 0)

p = Punto(1, 2, 3) 
print(p) 
p = Punto2D(1, 2) 
print(p)
# Solucion: Punto A (1, 2, 3) Punto2D B (1, 2)