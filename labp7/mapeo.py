#===================
# Función pura x**2
#===================

def alcuadrado(x):
    return x*x

#====================
# Función pura x***3
#====================

def alcubo(x):
    return x*x*x

#==========================
# Mapeo de una funciónpura
#==========================

def mapeo(func,lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado,[2.5,2,3.8,1.2,6.6,1j,7,8,])
cubos = mapeo(alcubo,[1,2,3,4,5,6,7,8])
print(cuadrados)
print(cubos)
