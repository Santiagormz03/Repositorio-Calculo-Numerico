import math
#Nombre: Santiago Ramirez C.I: 31.455.345
def newton_raphson(f, df, x0, er, n):
    ei = 1.00           # Error iterativo inicial
    i = 0               # Contador de iteraciones
    x_anterior = x0

    print(f"{'Iter':<5} | {'Raiz':<12} | {'Error':<12}")
    print("-" * 35)

    while (ei > er) and (i < n):
        derivada = df(x_anterior)
        
        if derivada == 0:
            print("Error: La derivada es cero. No se puede continuar.")
            return None, None

        # Fórmula: x_n+1 = x_n - f(x_n) / f'(x_n)
        x_actual = x_anterior - f(x_anterior) / derivada
        
        if x_actual != 0:
            ei = math.fabs((x_actual - x_anterior) / x_actual)
        
        print(f"{i+1:<5} | {x_actual:<12.7f} | {ei:<12.4f}")
        
        x_anterior = x_actual
        i += 1

    return x_actual, ei

if __name__ == "__main__":
    # Ejemplo: f(x) = x^2 - 2 (Buscando la raíz de 2)
    # f'(x) = 2x
    funcion = lambda x: x**2 - 2
    derivada = lambda x: 2*x
    
    punto_inicial = 1.5
    error_maximo = 0.0001
    max_iteraciones = 50
    
    raiz, error_final = newton_raphson(funcion, derivada, punto_inicial, error_maximo, max_iteraciones)
    
    if raiz is not None:
        print("-" * 35)
        print(f"Resultado Final: {raiz:.7f}")