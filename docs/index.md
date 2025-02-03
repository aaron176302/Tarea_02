# Welcome to Tarea#2

# Introducción al Problema

El objetivo es dar solución a una integral definida utilizando el *método de cuadratura Gaussiana, que es un enfoque numérico eficiente para la aproximación de integrales. Este método se basa en el uso de los **polinomios de Legendre*, los cuales permiten obtener una aproximación precisa de la integral al seleccionar puntos específicos dentro del intervalo de integración.

El problema consiste en resolver la siguiente integral definida:

$$
I = \int_{1}^{3} \left( x^6 - x^2 \sin(2x) \right) \, dx
$$

Este tipo de integrales, que involucra polinomios y funciones trigonométricas, puede ser difícil de evaluar de manera analítica. Por ello, se utiliza la cuadratura Gaussiana para aproximar el valor de la integral con una precisión cada vez mayor al aumentar el número de puntos de evaluación \( N \).

El objetivo de este ejercicio es determinar el valor de \( N \) necesario para que la aproximación de la integral utilizando la cuadratura Gaussiana coincida con el valor exacto de la integral. Para ello, se emplearán las rutinas y conceptos aprendidos en clase, específicamente en el tema sobre *Gaussian Quadrature*.
