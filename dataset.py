# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Wed Aug 16 00:14:27 2017

@author: Raynier
"""
import random

from perceptron import Perceptron

## Data de los sensores y la camara
input_data = [[40,60,60,0], #[SensorRight,SensorLeft,Camara]
              [41,58,55,0],
              [37,55,50,0],
              [70,63,47,0],
              [31,43,33,0],
              [32,30,49,0],
              [55,70,128,1],
              [38,15,44,1],
              [62,25,95,1],
              [15,50,36,1],
              [27,43,121,1],
              [18,23,48,1],
              [25,10,100,1]]


## Creamos el perceptron
pr = Perceptron(4) # Perceptron con 4 entradas
weights = [] # Lista con los pesos
errors = []  # Lista con los errores

## Fase de entrenamiento
for _ in range(1000):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1] # Agregamos un uno por default
        weights.append(pr._w)
        err = pr.train(inp,output)
        errors.append(err)

##  Veces que se agregaran entradas a la red
for i in range(70):

    sensor_right = random.randint(0,70) # Numeros aleatorios de 0 al 70 cm que representan la data del sensor derecho

    sensor_left = random.randint(0,70) # Numeros aleatorios de 0 al 70 cm que representan la data del sensor izquierdo

    cam = random.randint(32,128) # Numeros aleatorios que representan la cantidad de pixeles de la imagen captada por la camara

    h,w,c = [sensor_right, sensor_left,cam] # Asignacion de la data de los sensores y la camara a las variables h,w,c


    if pr.predict([1,h,w,c]) == 1:
        print ("NAO esquiva obstaculo")
    else:
        print("NAO camina")


#Nota: El resultado puede estar incorrecto.
#Esto puede ser debido a sesgo en la muestra, o porque es imposible separar
#a hombres y mujeres perfectamente basados unicamente en talla y peso."""

## Fase de graficacion
import imp

can_plot = True
try:
    imp.find_module('matplotlib')
except:
    can_plot = False

if not can_plot:
    print ("No es posible graficar los resultados porque no tienes matplotlib")
    sys.exit(0)
    pass

import matplotlib.pyplot as plt

plt.plot(errors)
plt.show()
