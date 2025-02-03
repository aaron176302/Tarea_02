# Explanation
 

##Descripción del Método, cuadratura Gaussiana con Polinomios de Legendre.

Es un método de integración numérica que permite aproximar integrales definidas de manera precisa. En lugar de usar una simple división del intervalo y aplicar un promedio, la cuadratura Gaussiana elige puntos específicos dentro del intervalo para evaluar la función, llamamos puntos de muestreo o x_{k}, y asigna un peso o w_{k} a cada uno de esos puntos. Los polinomios de Legendre se utilizan para determinar estos puntos y pesos de manera que la aproximación sea lo más precisa posible, especialmente para polinomios de alto grado.

- Los puntos de muestreo se escogen de manera tal que no son equidistantes. Esto introduce más grados de libertad para la misma discretización en 𝑁 subregiones.

- Es exacta para un polinomio de orden (2𝑁−1).

- Es decir, la cuadratura Gaussiana da la misma precisión que un polinomio de orden (2𝑁−1).

- Los pesos se eligen tal que:
    $$
        𝑤𝑘 = \[\frac{2}{(1 - 𝑥^2)\left(\frac{d𝑃𝑁}{d𝑥}\right)^2}\],  𝑥=𝑥𝑘
    $$
, con 𝑥𝑘 que cumple 𝑃𝑁(𝑥𝑘)=0

Para usar la cuadratura Gaussiana, primero se realiza una transformación del intervalo de integración, si es necesario, para que esté en el rango estándar [−1,1]. Luego, se calculan los puntos de muetreo (los ceros de los polinomios de Legendre) y sus respectivos pesos, que nos indican qué tan importante es cada punto en la aproximación de la integral. A continuación, se evalúa la función en estos puntos de Gauss y se multiplica cada valor por el peso correspondiente. Finalmente, se suman los resultados ponderados para obtener la aproximación de la integral.
