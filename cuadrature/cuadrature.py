from scipy.special import legendre
import numpy as np


def gaussxw(N):
    """
    Calcula los puntos y pesos para la cuadratura de Gauss-Legendre de orden N.

    Esta función utiliza un método iterativo para encontrar los puntos (raíces) y los pesos correspondientes
    de la cuadratura de Gauss-Legendre. Los puntos corresponden a las raíces del polinomio de Legendre de grado N,
    y los pesos se calculan a partir de esas raíces.

    Args:
        N (int): El número de puntos (y pesos) para la cuadratura de Gauss-Legendre.

    Returns:
        tuple: Un tuple que contiene:
            - x (np.ndarray): Un arreglo de puntos (raíces) de la cuadratura.
            - w (np.ndarray): Un arreglo de pesos correspondientes a esos puntos.
    """

    a = np.linspace(3, 4 * (N - 1), N) / ((4 * N) + 2)

    x = np.cos(np.pi * a + 1 / (8 * N * N * np.tan(a)))

    epsilon = 1e-15
   
    delta = 1.0
    while delta > epsilon:
        p0 = np.ones(N, dtype = float)

        p1 = np.copy(x)
        for k in range(1, N):
            p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        dp = (N + 1) * (p0 - x * p1) / (1 - x * x)
        dx = p1 / dp
        x -= dx
        delta = np.max(np.abs(dx))

    w = 2 * (N + 1) * (N + 1)/(N * N * (1 - x * x) * dp * dp)

    return x,w

def gaussxwab(a, b, x, w):
    """
    Escala los puntos y pesos de la cuadratura de Gauss-Legendre al intervalo [a, b].

    Esta función transforma los puntos y pesos calculados en el intervalo estándar [-1, 1] a un intervalo arbitrario [a, b].

    Args:
        a (float): El límite inferior del intervalo.
        b (float): El límite superior del intervalo.
        x (np.ndarray): Los puntos de la cuadratura en el intervalo estándar [-1, 1].
        w (np.ndarray): Los pesos correspondientes a los puntos en el intervalo estándar [-1, 1].

    Returns:
        tuple: Un tuple que contiene:
            - x (np.ndarray): Los puntos escalados al intervalo [a, b].
            - w (np.ndarray): Los pesos escalados correspondientes.
    """

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

puntos2_pesos2 = gaussxw(2)

puntos3_pesos3 = gaussxw(3)

puntos4_pesos4 = gaussxw(4) 


puntos2_pesos2_escalado = gaussxwab(1, 3, puntos2_pesos2[0], puntos2_pesos2[1])

puntos3_pesos3_escalado = gaussxwab(1, 3, puntos3_pesos3[0], puntos3_pesos3[1])

puntos4_pesos4_escalado = gaussxwab(1, 3, puntos4_pesos4[0], puntos4_pesos4[1])

def funcion(x):
    """
    Define una función matemática arbitraria a evaluar en la cuadratura.

    Esta función puede ser modificada según las necesidades del problema, en este caso
    se evalúa una función de ejemplo f(x) = x^6 - x^2 * sin(2x).

    Args:
        x (np.ndarray): Un arreglo de puntos donde se evaluará la función.

    Returns:
        np.ndarray: El valor de la función evaluada en los puntos x.
    """

    return (x**6) - x**2*np.sin(2*x)
 
def sumatoria(puntos_pesos_escalado, funcion):
    """
    Realiza la sumatoria ponderada para aproximar la integral utilizando la cuadratura de Gauss-Legendre.

    Esta función aplica los puntos y pesos escalados a la función proporcionada y calcula la suma ponderada,
    que es una aproximación de la integral definida.

    Args:
        puntos_pesos_escalado (tuple): Un tuple que contiene:
            - x (np.ndarray): Los puntos escalados.
            - w (np.ndarray): Los pesos escalados correspondientes.
        funcion (function): La función a integrar.

    Returns:
        float: El resultado de la integral aproximada.
    """

    resultado_N = np.sum(funcion(puntos_pesos_escalado[0])*puntos_pesos_escalado[1])

    return resultado_N

resultado_integral_N2 = sumatoria(puntos2_pesos2_escalado, funcion)

print(f"el resultado para N=2 {resultado_integral_N2}")

resultado_integral_N3 = sumatoria(puntos3_pesos3_escalado, funcion) 

print(f"el resultado para N=3 {resultado_integral_N3}")

resultado_integral_N4 = sumatoria(puntos4_pesos4_escalado, funcion)

print(f"el resultado para N=4 {resultado_integral_N4}, resultado correcto")

