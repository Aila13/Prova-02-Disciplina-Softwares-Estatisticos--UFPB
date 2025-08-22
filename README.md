# Projeto 2: Estatística NumPy

Biblioteca foi desenvolvida como atividade prática da disciplina **Introdução aos Softwares EstatÍsticos**, explorando os módulos `numpy.random` e `numpy.linalg`.

---

## Objetivo


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
O arquivo main.py demonstra como utilizar todas as funcionalidades da biblioteca. Para rodar o exemplo, basta executar o script.
Instruções de instalação
git clone https://github.com/SEU_USUARIO/estatistica_numpy.git
cd estatistica_numpy
python main.py
