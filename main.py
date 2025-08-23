import Pacotes as pct
import numpy as np

def main():
    # Parte 1: Simulação de dados (random) 
    dados = pct.simula_dados_normais(1000, media=50, desvio=10)
    print("Primeiros 10 dados simulados (Normal):", dados[:10])

    # Parte 2: Medidas estatísticas 
    print("\nMédia:", pct.media(dados))
    print("Mediana:", pct.mediana(dados))
    print("Variância:", pct.variancia(dados))
    print("Desvio padrão:", pct.desvio_padrao(dados))

    # Parte 3: Sistema linear com linalg ---
    A = np.array([[2, 1], [1, 3]])
    b = np.array([8, 13])
    solucao = pct.resolver_sistema(A, b)
    print("\nSolução do sistema Ax=b:", solucao)

    # Parte 4: Autovalores e autovetores ---
    M = np.array([[4, 2], [1, 3]])
    valores, vetores = pct.autovalores_autovetores(M)
    print("\nAutovalores:", valores)
    print("Autovetores:\n", vetores)

if __name__ == "__main__":
    main()
