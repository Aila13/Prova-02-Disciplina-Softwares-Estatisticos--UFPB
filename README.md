# Projeto 2: Estatística NumPy

Biblioteca foi desenvolvida como atividade prática da disciplina **Introdução aos Softwares EstatÍsticos**, explorando os módulos `numpy.random` e `numpy.linalg`.

---

## Objetivo

O objetivo desta biblioteca é aprimorar o domínio de Python e NumPy por meio de um projeto prático. Que foi desenvolvido para demonstrar a geração de dados aleatórios utilizando o submódulo `numpy.random` e a solução de problemas de álgebra linear com o `numpy.linalg`

---

## Funcionalidades implementadas

### Estatística descritiva (`medidas.py`)
- `media(dados)` → calcula a média
- `mediana(dados)` → calcula a mediana
- `variancia(dados)` → calcula a variância
- `desvio_padrao(dados)` → calcula o desvio padrão

### Simulação de dados (`simulacao.py`)
- `simula_dados_normais(n, media, desvio)` → gera `n` observações de uma Normal(μ, σ)
- `simula_dados_binomiais(n, tentativas, p)` → gera `n` observações de uma Binomial(n, p)

### Álgebra linear (`linear.py`)
- `resolver_sistema(A, b)` → resolve um sistema linear Ax = b
- `autovalores_autovetores(M)` → calcula autovalores e autovetores de uma matriz

---

## Exemplos de Uso
O arquivo `main.py` demonstra como utilizar todas as funcionalidades da biblioteca. Para rodar o exemplo, basta executar o script.

---

## Instruções de instalação
### clonar este repositório para o seu ambiente local:

- git clone https://github.com/Aila13/Prova-02-Disciplina-Softwares-Estatisticos--UFPB.git

### Assegure-se de que a biblioteca NumPy esteja instalada:

- pip install numpy

### Execute o arquivo main.py

---

## Autor
Aila Ferreira

Discente de Estatística - UFPB
