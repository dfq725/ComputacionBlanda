#Paquetes Requeridos

import numpy as np 
import skfuzzy as sk 
import matplotlib.pyplot as plt 
%matplotlib inline

# Se define un array x para el manejo del factor de calidad en un restaurante
x = np.arange (30, 80, 0.1)

# se define array para la funcion miembro de tipo Triangular
lento = fuzz.trimf(x, [30,30,50])
medio = fuzz.trimf(x, [30,50,70])
medio_rapido = fuzz.trimf(x, [50,60,80])
rapido = fuzz.trimf(x, [60,60,80])

# Se grafica la funcion de Membresia
plt.figure()
plt.plot(x, rapido, 'b', linewidth=1.5, label='Rapido')
plt.plot(x, medio_rapido, 'k', linewidth=1.5, label='Medio-Rapido')
plt.plot(x, medio, 'm', linewidth=1.5, label='Medio')
plt.plot(x, lento, 'r', linewidth=1.5, label='Lento')

plt.title('Penalti Difuso')
plt.ylabel('Membresia')
plt.xlabel('Velocidad (km/h)')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5),ncol=1, fancybox=True, shadow=True)
plt.show()