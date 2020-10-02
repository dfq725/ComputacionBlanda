#Daniel Quintero 1088328360

""" =========================================
si quiere tener el resultado de un pantallazo en especifico, descomente la seccion 
segun la parte deseada.
EJEMPLO: busco el resultado de CapturaDeML02_3, descomento la seccion 3
========================================= """

# Se importa la librería numpy
import numpy as np

# APILAMIENTO
# -----------
# Apilado
# Las matrices se pueden apilar horizontalmente, en profundidad o
# verticalmente. Podemos utilizar, para ese propósito,
# las funciones vstack, dstack, hstack, column_stack, row_stack y concatenate.
# Para empezar, vamos a crear dos arrays
# Matriz a


""" 
a = np.arange(9).reshape(3,3)
print('a =\n', a, '\n')

# Matriz b, creada a partir de la matriz a
b = a*2
print('b =\n', b)

# Utilizaremos estas dos matrices para mostrar los mecanismos
# de apilamiento disponibles """


""" # Seleccionando elementos de un array
a = np.array([[1,2], [3,4]])
print('a =\n', a, '\n')
# Elementos individuales
print('a[0,0] =', a[0,0], '\n')
print('a[0,1] =', a[0,1], '\n')
print('a[1,0] =', a[1,0], '\n')
print('a[1,1] =', a[1,1]) """


""" # Crea un array con 9 elementos, desde 0 hasta 8
a = np.arange(9)
print('a =', a, '\n')
# Muestra los elementos desde 0 hasta 9. Imprime desde 0 hasta 8
print('a[0:9] = ', a[0:9], '\n')
# Muestra desde 3 hasta 7. Imprime desde 3 hasta 6
print('a[3,7] =', a[3:7], '\n')
# Mostrando todos los elementos, desde el 0 hasta el 8, de uno en uno
print('a[0:9:1] =', a[0:9:1], '\n')
# El mismo ejemplo, pero omitiendo el número 0 al principio, el cual no es necesario aquí
print('a[:9:1] =', a[:9:1], '\n')
# Mostrando los números, de dos en dos
print('a[0:9:2] =', a[0:9:2], '\n')
# Mostrando los números, de tres en tres
print('a[0:9:3] =', a[0:9:3])
# Si utilizamos un incremento negativo, el array se muestra en orden inverso
# El problema es que no muestra el valor 0
print('a[9:0:-1] =', a[9:0:-1], '\n')
# Si se omiten los valores de índice, el resultado es preciso
print('a[::-1] =', a[::-1]) """


""" # Utilización de arreglos multidimensionales
b = np.arange(24).reshape(2,3,4)
print('b =\n', b,'\n')
# La instrucción reshape genera una matriz con 2 bloques, 3 filas y 4 columnas
# El número total de elementos es de 24 (generados por arange)

# Acceso individual a los elementos del array
# Elemento en el bloque 1, fila 2, columna 3
print('b[1,2,3] =', b[1,2,3], '\n')
# Elemento en el bloque 0, fila 2, columna 2
print('b[0,2,2] =', b[0,2,2], '\n')
# Elemento en el bloque 0, fila 1, columna 1
print('b[0,1,1] =', b[0,1,1],'\n')

# Mostraremos como generalizar una selección
# Primero elegimos el componente en la fila 0, columna 0, del bloque 0
print('b[0,0,0] =', b[0,0,0], '\n')
# A continuación, elegimos el componente en la fila 0, columna, pero del bloque 1
print('b[1,0,0] =', b[1,0,0], '\n')
# Para elegir SIMULTANEAMENTE ambos elementos, lo hacemos utilizando dos puntos
print('b[:,0,0] =', b[:,0,0], '\n')

# Si escribimos: b[0]
# Habremos elegido el primer bloque, pero habríamos omitido las filas y las columnas
# En tal caso, numpy toma todas las filas y columnas del bloque 0
print('b[0] =\n', b[0],'\n')

# Cuando se utiliza la notación de : a derecha o a izquierda, se puede reemplazar por ...
# El ejemplo anterior se puede escribir así:
print('b[0, ...] =\n', b[0, ...],'\n')

# Si queremos la fila 1 en el bloque 0 (sin que importen las columnas), se tiene:
print('b[0,1] =', b[0,1]) """

# El resultado de una selección puede utilizar luego para un cálculo posterior
# Se obtiene la fila 1 del bloque 0 (como en ejemplo anterior) y se asigna dicha respuesta a la variable z
b = np.arange(24).reshape(2,3,4)
z = b[0,1]
print('z =', z, '\n')
# En este caso, la variable z toma el valor: [4 5 6 7]
# Si ahora queremos tomar de dicha respuesta los valores de 2 en 2, se tiene:
print('z[::2] =', z[::2],'\n')

# El ejercicio anterior se puede combinar en una expresión única, así:
print('b[0,1,::2] =', b[0,1,::2],'\n')
# Esta es una solución más compacta

# Imprime todas las columnas, independientemente de los bloques y filas
print(b, '\n')
print('b[:,:,1] =\n', b[:,:,1], '\n')
# Variante de notación (simplificada)
print('b[...,1] =\n', b[...,1],'\n')

# Si queremos seleccionar todas las filas 2, independientemente de los bloques y columnas, se tiene:
print(b, '\n')
print('b[:,1] =', b[:,1],'\n')
# Puesto que no se menciona en la notación las columnas, se toman todos los valores según corresponda

# En el siguiente ejemplo seleccionmos la columna 1 del bloque 0
print(b, '\n')
print('b[0,:,1] =', b[0,:,1],'\n')