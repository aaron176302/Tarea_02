# Tutorials

Modo de uso:

La función gaussxw es invocada con un parámetro, el cual usted elije, ese sería su N, en esta parte lo podemos realizar de forma interactiva osea que el programa le solicite el valor de N al usuario, luego con este valor la función da como resultado una tupla, ejemplo:

puntos_pesos_escalada= gaussxw(6)

Luego con la función gaussxwab escalamos, por ejemplo: tupla_escalada= gaussxwab(1,3,puntos_pesos_escalada[0], puntos_pesos_escalados[1])

Estos resultados son muy importantes para invocar la función funcion() con estos valores, y así esta nos proporciona el valor de la integral.

Dicha función es:

$$
\int_1^3 \left( x^6 - x^2 \sin(2x) \right) \, dx
$$
 
Luego de esto solo toca, realizar el mismo procedimiento para diferentes N, hasta que la integral posea la precisión deseada.

