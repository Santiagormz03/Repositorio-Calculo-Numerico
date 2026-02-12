import math
#Nombre: Santiago Ramirez C.I: 31.455.345
def riemann(f, a, b, n):
    # 1. Calcular el ancho de cada rectángulo (delta x)
    h = (b - a) / n
    suma_areas = 0

    print(f"Calculando integral en el intervalo [{a}, {b}] con {n} rectángulos...")
    print("-" * 50)

    # 2. Sumar las áreas de todos los rectángulos
    for i in range(1, n + 1):
        # xi es el punto en el extremo derecho del rectángulo actual
        xi = a + i * h
        suma_areas += f(xi)

    # 3. Multiplicar la suma de las alturas por la base (h)
    resultado = h * suma_areas
    return resultado

if __name__ == "__main__":
    # Ejemplo: Calcular la integral de f(x) = x^2 desde 0 hasta 1
    # El resultado exacto es 1/3 (0.3333333...)
    
    f = lambda x: x**2
    a = 0
    b = 1
    n = 1000  # Prueba cambiando n a 10, 100 o 10000 para ver cómo mejora
    
    area_total = riemann(f, a, b, n)
    
    print("Realizado por: Santiago Ramirez C.I:31.455.345. Sección 0520")
    print(f"Resultado de la aproximación: {area_total:0.7f}")
    print(f"Error aproximado: {math.fabs(0.3333333 - area_total):0.7f}")
    print("-" * 50)