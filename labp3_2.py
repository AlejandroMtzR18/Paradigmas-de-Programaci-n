#================
# Primera función
#================

def saludo():
    #====================================
    # Documenetación rápida de la función
    #====================================
    """Esta función saluda"""
    print('¡Quiúbules!, ¿cómo estás?')


#======================
# Llamado de la función 
#======================

saludo()

#=============================
# Se ejecuta pero no se asigna
#=============================

salida = saludo()


#=================
# Esto no funciona
#=================

print(salida)

#======================
# Mostrar documentación 
#======================

#help(saludo)

#======================
# Función con argumento
#======================

def salu2(nombre):
    """Esta funcion te saluda por tu nombre"""
    print("¡Qué onda ese", nombre, "!")
salu2("Julian")
salu2("Alejandro")

#=========================================
# Ahorrar trabajo del intérprete 
# nombre: str la variable nombre es un str
#=========================================

def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("!Que onda ese", nombre,"!")
saludos("Alejandro")
a = 123
print(type(a))
saludos(a)

#==============================
# Función con muchos argumentos
#==============================

def saludos_multiples(nombre1,nombre2,nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("hola",nombre1,",",nombre2,"y" ,nombre3)
saludos_multiples("Hugo","Paco","Luis")

#===========================================
# Función con cualquier número de argumentos
#===========================================

def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0
    #=================================
    # end = es para ponerlo de corrido
    #=================================
    print("Hola",end="")
    while len(nombres) > i: #len = longitud
        # Ultimo nombre
        if(i==len(nombres)-1):
          print(nombres[i])
        else:
            #Cualquier otro nombre
            print(nombres[i], end=", ")
            i+=1

muchos_saludos("Bosco","Angel","David","Tamara","Mili","Edwin","Lev","Luis","Abigail")

def greet(firstname, lastname):
    print('Hello',firstname, lastname)

#=============================================
# Llamar la función con argumentos en desorden
#=============================================

greet(lastname='Jobs',firstname='Steve') #Se puedes especificar las variables en desorden

#=======================
# Función con argumentos
#=======================

def greet(**person):
    #===================================================
    # Persona tiene características firstname y lastname
    #===================================================
    print('Hello',person['firstname'], person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55) # se pueden pasar más parámetros de los necesarios

#============================
# Función valores por defecto
#============================

def greet(name='Guest'):
    print('Hello',name)

greet() #Utiliza el valor dado de antemano 
greet('Steve')

#======================
# Función con resultado
#======================

def suma(a,b):
    return a+b

#=================================
# Programación funcional
# Se pueden funciones en funciones
#=================================

total = suma(5, suma(10,20))
print(total)

#=================================================
# Cálculo lambda
# nombre de la función = lambda variable : función
#=================================================

x_al_cuadrado = lambda x : x * x
al = x_al_cuadrado(5)
print(al)

#===========================
# lambda de varias variables
#===========================

suma= lambda x1, x2, x3: x1+x2+x3
print(sumas(100,200,300,400))

#=======================================
# Uso de una función anónima
# El argumento va fuera entre paréntesis
#=======================================

print((lambda x: x*x)(6)) #función anónima

#============================
# Función con variable global
# EVITE EL EXCESO !!!!
#============================

name = 'Steve'
def greet():
    global name #Para utilizar una variable global (que viene fuera del bloque)

greet()














