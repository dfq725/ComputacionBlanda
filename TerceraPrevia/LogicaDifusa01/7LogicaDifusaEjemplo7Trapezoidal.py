#funcion de Membresia trapezoidal

import numpy as np 
import skfuzzy as sk 
import matplotlib.pyplot as plt 

# Se define un array x para el manejo del factor de calidad en un restaurante
x = np.arange (0, 11, 1)

# se define array para la funcion miembro de tipo Triangular
vd_trapezoidal = sk.trapmf(x, [0,3,5,8])

# Se grafica la funcion de Membresia
plt.figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='sevicio')

plt.title('calidad del Servicio en un Restaurante')
plt.ylabel('Membresia')
plt.xlabel('Nivel de Servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5),ncol=1, fancybox=True, shadow=True)
plt.show()