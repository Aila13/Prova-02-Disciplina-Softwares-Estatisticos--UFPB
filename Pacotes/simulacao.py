import numpy as np

def simula_dados_normais(n, media=0, desvio=1):
    """Simula n dados de uma Normal(media, desvio)"""
    return np.random.normal(media, desvio, n)

def simula_dados_binomiais(n, tentativas=10, p=0.5):
    """Simula n dados de uma Binomial(tentativas, p)"""
    return np.random.binomial(tentativas, p, n)
