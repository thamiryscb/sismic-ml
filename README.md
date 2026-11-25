# Agrupamento de Dados Sísmicos e Generalização entre Bacias Sedimentares

## Sobre o projeto

Este projeto investiga a aplicação de algoritmos de Machine Learning não supervisionado a dados sísmicos reais, com foco na identificação de padrões, no agrupamento de atributos sísmicos e na avaliação da capacidade de generalização entre diferentes bacias sedimentares.

O estudo propõe uma análise comparativa entre os algoritmos K-means e Gaussian Mixture Model (GMM), considerando a qualidade dos agrupamentos, a eficiência computacional e a capacidade de transferência dos padrões aprendidos para diferentes contextos geológicos.

## Objetivo geral

Avaliar o desempenho e a capacidade de generalização de modelos de Machine Learning não supervisionado aplicados ao agrupamento de dados sísmicos de diferentes bacias sedimentares.

## Objetivos específicos

- Realizar a análise exploratória dos dados sísmicos.
- Extrair e caracterizar diferentes atributos sísmicos.
- Aplicar técnicas de pré-processamento e padronização dos dados.
- Investigar a seleção de atributos e a redução de dimensionalidade por meio do PCA.
- Implementar os algoritmos K-means e GMM.
- Otimizar os hiperparâmetros dos modelos.
- Avaliar a qualidade e a estabilidade dos agrupamentos.
- Investigar a capacidade de generalização entre bacias sedimentares.
- Analisar a incerteza dos agrupamentos probabilísticos.
- Comparar o desempenho computacional dos algoritmos.

## Metodologia

O desenvolvimento do projeto está organizado nas seguintes etapas:

1. Aquisição e carregamento dos dados sísmicos.
2. Análise exploratória dos dados.
3. Extração de atributos sísmicos.
4. Separação dos conjuntos de treinamento e validação.
5. Pré-processamento e padronização.
6. Seleção de atributos e redução de dimensionalidade.
7. Seleção de hiperparâmetros.
8. Treinamento dos modelos K-means e GMM.
9. Validação interna dos modelos.
10. Aplicação dos modelos em outra bacia sedimentar.
11. Comparação das métricas e do desempenho computacional.
12. Análise e discussão dos resultados.

## Base de dados

Inicialmente, serão utilizados dados sísmicos pré-stack da Bacia do Jequitinhonha, localizada na margem continental brasileira.

Uma segunda base de dados sísmicos será selecionada para avaliar a capacidade de generalização dos modelos em diferentes contextos geológicos.

Os arquivos sísmicos originais não estão incluídos neste repositório devido ao seu tamanho e às possíveis restrições de utilização e distribuição.

## Atributos sísmicos

Os atributos inicialmente considerados para o desenvolvimento do projeto são:

- Amplitude sísmica;
- Envelope;
- Fase instantânea;
- Frequência instantânea;
- Amplitude RMS;
- Variância local.

Diferentes combinações desses atributos serão avaliadas para investigar sua influência na qualidade dos agrupamentos.

## Modelos de Machine Learning

### K-means

Algoritmo de aprendizado não supervisionado que realiza o agrupamento das amostras com base na distância aos centroides, buscando minimizar a dispersão interna dos clusters.

### Gaussian Mixture Model (GMM)

Modelo probabilístico que representa a distribuição dos dados por meio de uma combinação de distribuições gaussianas, permitindo estimar a probabilidade de pertencimento de cada amostra aos diferentes agrupamentos.

## Métricas de avaliação

- Coeficiente Silhouette;
- Índice Davies-Bouldin;
- Índice Calinski-Harabasz;
- Critério de Informação de Akaike (AIC), para o GMM;
- Critério de Informação Bayesiano (BIC), para o GMM;
- Estabilidade dos agrupamentos;
- Tempo de treinamento;
- Tempo de predição;
- Consumo de memória;
- Incerteza dos agrupamentos probabilísticos.

## Tecnologias utilizadas

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Scikit-learn
- Segyio
- Joblib
- Psutil
- Jupyter Notebook
- Visual Studio Code
- Git e GitHub

## Estrutura do projeto

```
seismic-ml-generalization/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── seismic_generalization.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── features.py
│   ├── preprocessing.py
│   ├── models.py
│   ├── evaluation.py
│   └── visualization.py
│
├── models/
│
├── results/
│   ├── figures/
│   └── metrics/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/thamiryscb/sismic-ml.git
```

### 2. Acessar a pasta do projeto

```bash
cd seismic-ml-generalization
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 5. Instalar as dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Adicionar os dados sísmicos

Inserir os arquivos sísmicos no formato SEG-Y na pasta:

```
data/raw/
```

### 7. Executar o notebook

Abrir o arquivo:

```
notebooks/seismic_generalization.ipynb
```

Selecionar o ambiente virtual criado como kernel do notebook e executar as células sequencialmente.

## Resultados esperados

Espera-se identificar padrões relevantes nos atributos sísmicos, comparar o desempenho dos algoritmos K-means e GMM e investigar a capacidade de generalização dos modelos quando aplicados a diferentes bacias sedimentares.

Os agrupamentos obtidos serão analisados considerando suas características estatísticas e geofísicas, respeitando as limitações da interpretação geológica sem dados independentes de validação.

## Otimização computacional

Com o objetivo de reduzir o consumo de recursos computacionais e facilitar a reprodução dos experimentos, o projeto utilizará técnicas como:

- Amostragem controlada dos dados.
- Processamento em blocos.
- Otimização do armazenamento de matrizes.
- Reutilização de funções Python.
- Visualizações gráficas estáticas.
- Armazenamento externo dos arquivos sísmicos.

## Contexto acadêmico

Projeto acadêmico desenvolvido no âmbito do estudo de Machine Learning aplicado a dados geológicos e geofísicos na Universidade Federal do Rio Grande do Norte (UFRN).
