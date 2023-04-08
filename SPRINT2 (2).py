#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import pandas as pd
import numpy as np

# Carga de la base de datos
data = pd.read_csv("Datos SPRINT2.csv")


# Funcion para definir la similitud coseno
def calcular_similitud():
    # Obtener los nombres seleccionados en las listas desplegables
    nombre1 = lista1.get()
    nombre2 = lista2.get()
    
    
    # Obtener los datos correspondientes a los nombres seleccionados
    datos1 = data[data['nombre'] == nombre1].iloc[:, 1:].values
    datos2 = data[data['nombre'] == nombre2].iloc[:, 1:].values
    
    # Calcular la similitud coseno entre los dos conjuntos de datos
    # Se usa el método .flatten para transformar los datos en una matriz tridimensional
    dot_product = np.dot(datos1.flatten(), datos2.flatten())
    
    # Se usa el método .linalg para calcular la norma Euclidiana de cada vector
    norm1 = np.linalg.norm(datos1)
    norm2 = np.linalg.norm(datos2)
    similitud = dot_product / (norm1 * norm2)
    
    # Mostrar el resultado en la etiqueta correspondiente
    resultado.config(text="La similitud coseno entre {} y {} es: {:.2f}".format(nombre1, nombre2, similitud))
    
    

# Crear la ventana principal y agregar los elementos
ventana = tk.Tk()
ventana.title("Calculadora de similitud coseno")


opciones = list(data['nombre'])
lista1 = tk.StringVar(ventana)
lista1.set(opciones[0])
menu1 = tk.OptionMenu(ventana, lista1, *opciones)
lista2 = tk.StringVar(ventana)
lista2.set(opciones[0])
menu2 = tk.OptionMenu(ventana, lista2, *opciones)

boton = tk.Button(ventana, text="Calcular similitud", command=calcular_similitud)

resultado = tk.Label(ventana, text="Seleccione dos nombres para calcular la similitud coseno")

menu1.pack()
menu2.pack()
boton.pack()
resultado.pack()


ventana.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




