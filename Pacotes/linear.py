import numpy as np

def resolver_sistema(a, b):
    """
    Resolve um sistema linear Ax = b
    A = matriz de coeficientes
    b = vetor de resultados
    """
    return np.linalg.solve(a, b)

def autovalores_autovetores(m):
    """
    Retorna autovalores e autovetores de uma matriz
    """
    valores, vetores = np.linalg.eig(m)
    return valores, vetores
