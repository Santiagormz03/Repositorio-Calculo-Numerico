import math

def biseccion(f, a, b, er, n):
    """Algoritmo de Bisección compatible con Windows."""
    ei = 1.00           
    i = 0               
    m_anterior = None  

    # Validar Teorema de Bolzano antes de empezar
    if f(a) * f(b) >= 0:
        print("Error: La función no cambia de signo en el intervalo dado.")
        return None, None

    while (ei > er) and (i < n):
        m_actual = (a + b) / 2

        if m_anterior is not None:
            ei = math.fabs((m_actual - m_anterior) / m_actual)

        if f(a) * f(m_actual) < 0:
            b = m_actual
        elif f(m_actual) * f(b) < 0:
            a = m_actual
        else:
            return m_actual, ei

        m_anterior = m_actual
        i += 1

    return m_actual, ei

if __name__ == "__main__":
    f = lambda x: math.exp(-x) - math.log(x)
    a, b, er, n = 1, 1.5, 0.01, 100
    
    raiz, error = biseccion(f, a, b, er, n)
    if raiz:
        print("Realizado por: Santiago Ramirez C.I:31.455.345. Sección 0520")
        print(f"--- Resultado Biseccion ---")
        print(f"Raiz: {raiz:0.7f}")
        print(f"Error: {error:0.4f}")