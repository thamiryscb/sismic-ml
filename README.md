# Machine Learning aplicado à Segmentação Sísmica e Generalização entre Bacias

## 1. Sobre o projeto

Este projeto apresenta uma aplicação de técnicas de Machine Learning não supervisionado a dados sísmicos reais das bacias sedimentares do Jequitinhonha e de Campos.

São utilizados os algoritmos K-means e Gaussian Mixture Model (GMM) para identificar agrupamentos de amostras sísmicas com características semelhantes, considerando os atributos de amplitude, envelope e fase instantânea.

O principal diferencial do trabalho consiste na avaliação da capacidade de generalização dos modelos, treinados exclusivamente com dados da Bacia do Jequitinhonha e posteriormente aplicados à Bacia de Campos, sem reajuste dos parâmetros aprendidos.

O projeto foi desenvolvido no contexto acadêmico da Universidade Federal do Rio Grande do Norte (UFRN).

## 2. Objetivos

### Objetivo geral

Desenvolver e avaliar modelos de Machine Learning não supervisionado para segmentação de dados sísmicos reais, investigando sua capacidade de generalização entre diferentes bacias sedimentares.

### Objetivos específicos

- Realizar a análise exploratória dos dados sísmicos.
- Extrair e analisar atributos sísmicos.
- Implementar os algoritmos K-means e GMM.
- Investigar diferentes configurações de hiperparâmetros.
- Comparar quantitativamente e visualmente os agrupamentos.
- Avaliar os modelos utilizando dados de validação interna.
- Investigar a generalização dos modelos para a Bacia de Campos.
- Comparar o desempenho computacional dos algoritmos.

## 3. Conjuntos de dados

São utilizados dados sísmicos reais no formato SEG-Y.

| Característica | Jequitinhonha | Campos |
|---|---:|---:|
| Número de traços | 12.060 | 9.552 |
| Amostras por traço | 1.001 | 1.501 |
| Intervalo de amostragem | 4 ms | 4 ms |
| Finalidade | Treinamento, ajuste e validação interna | Teste externo |

Os dados da Bacia do Jequitinhonha são divididos em três conjuntos:

- Treinamento: 64% dos traços.
- Ajuste de hiperparâmetros: 16% dos traços.
- Validação interna: 20% dos traços.

Os dados da Bacia de Campos são reservados para a avaliação externa dos modelos.

Os arquivos sísmicos originais não estão incluídos no repositório devido ao tamanho dos arquivos e à necessidade de verificar suas condições de redistribuição.

## 4. Metodologia

### 4.1. Pré-processamento e extração de atributos

Inicialmente, são realizados o carregamento, a análise exploratória e a normalização individual dos traços sísmicos.

A extração de atributos considera:

- Amplitude.
- Envelope instantâneo.
- Fase instantânea.
- Frequência instantânea.
- RMS.
- Variância local.

Para o treinamento definitivo dos modelos, são selecionados os atributos de amplitude, envelope e fase instantânea.

A padronização é realizada utilizando o StandardScaler, ajustado exclusivamente sobre as amostras de treinamento.

### 4.2. K-means

O algoritmo K-means é utilizado para identificar agrupamentos a partir da minimização das distâncias quadráticas entre as amostras e seus respectivos centroides.

São considerados:

- Inicialização k-means++.
- Diferentes números de clusters, variando entre 2 e 9.
- Método do cotovelo.
- Coeficiente de Silhouette.
- Caracterização estatística dos centroides.
- Distribuição percentual dos agrupamentos.
- Segmentação sísmica.

### 4.3. Gaussian Mixture Model (GMM)

O GMM representa os dados por meio de uma combinação de distribuições gaussianas multivariadas.

São considerados:

- Matrizes de covariância completas.
- Diferentes números de componentes, variando entre 2 e 9.
- Algoritmo Expectation-Maximization (EM).
- Critério de Informação de Akaike (AIC).
- Critério de Informação Bayesiano (BIC).
- Probabilidades de pertencimento.
- Entropia normalizada.
- Segmentação sísmica probabilística por atribuição à componente de maior probabilidade.

### 4.4. Validação interna

Os modelos são avaliados utilizando amostras da Bacia do Jequitinhonha provenientes de traços que não participaram do treinamento ou da seleção de hiperparâmetros.

A avaliação considera:

- Coeficiente de Silhouette.
- Índice Davies-Bouldin.
- Índice Calinski-Harabasz.
- Adjusted Rand Index (ARI).
- Normalized Mutual Information (NMI).
- Distribuição percentual dos agrupamentos.
- Comparação dos algoritmos com o mesmo número de clusters.
- Comparação visual das segmentações sísmicas.

### 4.5. Generalização entre bacias

Os modelos treinados na Bacia do Jequitinhonha são aplicados aos dados da Bacia de Campos, mantendo fixos os parâmetros dos algoritmos e do padronizador.

São analisados:

- Variação das métricas de agrupamento.
- Mudanças nas distribuições dos clusters.
- Distância de variação total.
- Distância aos centroides do K-means.
- Log-verossimilhança do GMM.
- Probabilidades de pertencimento e entropia.
- Identificação exploratória de amostras atípicas.
- Comparação visual das segmentações.

### 4.6. Desempenho computacional

A comparação do desempenho computacional considera os tempos observados de treinamento e de segmentação dos modelos nas duas bacias sedimentares.

## 5. Tecnologias utilizadas

- Python
- Jupyter Notebook
- NumPy
- Pandas
- SciPy
- Scikit-learn
- Matplotlib
- Visual Studio Code
- Git e GitHub

## 6. Estrutura do projeto

Principais arquivos e diretórios:

```text
sismic-ml/
│
├── data/
│   ├── raw/
│   │   ├── jequitinhonha.sgy
│   │   └── campos.sgy
│   └── processed/
│
├── notebooks/
│   └── seismic_generalization.ipynb
│
├── src/
│   ├── data_loader.py
│   └── features.py
│
├── models/
├── results/
│
├── .gitignore
├── .gitattributes
├── requirements.txt
└── README.md
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `seismic_generalization.ipynb` | Notebook principal contendo a metodologia, os experimentos e as análises |
| `data_loader.py` | Funções auxiliares para carregamento dos dados SEG-Y |
| `features.py` | Funções de normalização e extração dos atributos sísmicos |
| `requirements.txt` | Dependências necessárias para execução do projeto |
| `.gitignore` | Configuração dos arquivos excluídos do versionamento |
| `.gitattributes` | Configuração dos filtros de versionamento dos notebooks |

Os diretórios de dados, modelos e resultados podem não estar presentes na versão disponibilizada no GitHub, pois parte desses arquivos é mantida exclusivamente no ambiente local.

## 7. Como executar o projeto

### 7.1. Clonar o repositório

```bash
git clone https://github.com/thamiryscb/sismic-ml.git
cd sismic-ml
```

### 7.2. Criar um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 7.3. Instalar as dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 7.4. Disponibilizar os dados sísmicos

Crie o diretório `data/raw/`, caso ele não exista, e insira os arquivos SEG-Y com os seguintes nomes:

```text
data/raw/jequitinhonha.sgy
data/raw/campos.sgy
```

Os arquivos originais devem ser obtidos separadamente.

### 7.5. Abrir o projeto no Visual Studio Code

Na pasta principal do projeto, execute:

```bash
code .
```

Certifique-se de que as extensões Python e Jupyter estejam instaladas no Visual Studio Code.

### 7.6. Executar o notebook

Abra o arquivo:

```text
notebooks/seismic_generalization.ipynb
```

Selecione o kernel Python correspondente ao ambiente virtual `.venv`.

Garanta que o diretório de trabalho do notebook seja a pasta `notebooks/`.

Em seguida, utilize a opção **Run All** para executar todas as células sequencialmente.

A execução realiza o carregamento dos dados, o pré-processamento, o treinamento dos modelos, a validação interna, a generalização entre bacias e a geração das figuras.

## 8. Organização do notebook

| Etapa | Descrição |
|---:|---|
| 1 | Introdução |
| 2 | Configurações e bibliotecas |
| 3 | Carregamento dos dados sísmicos |
| 4 | Análise exploratória |
| 5 | Extração dos atributos sísmicos |
| 6 | Separação e pré-processamento dos dados |
| 7 | Seleção e preparação dos atributos |
| 8 | Aplicação do K-means |
| 9 | Aplicação do GMM |
| 10 | Validação interna e comparação dos modelos |
| 11 | Generalização para a Bacia de Campos |
| 12 | Análise do desempenho computacional |

## 9. Resultados e visualizações

O notebook permite gerar:

- Gráficos de amplitude e atributos sísmicos.
- Gráficos do método do cotovelo e da Silhouette.
- Gráficos dos critérios AIC e BIC.
- Caracterização estatística dos agrupamentos.
- Visualizações bidimensionais e tridimensionais.
- Mapas de segmentação sísmica.
- Visualizações individuais dos clusters.
- Comparação das métricas de validação interna.
- Comparação da generalização entre as bacias.
- Análise das probabilidades e incertezas.
- Comparação dos tempos de execução.

As saídas das células do notebook são removidas da versão disponibilizada no GitHub por meio do nbstripout, reduzindo o tamanho do repositório e evitando o versionamento de resultados gerados durante a execução.

## 10. Limitações

Os agrupamentos identificados representam similaridades matemáticas entre atributos sísmicos, não constituindo diretamente uma classificação geológica validada.

Diferenças observadas entre as bacias podem decorrer tanto de características geológicas quanto de condições de aquisição e processamento dos dados.

Além disso, a normalização individual dos traços reduz diferenças de escala, mas limita a interpretação das amplitudes absolutas.

## 11. Contexto acadêmico

Projeto desenvolvido no âmbito da graduação em Engenharia de Computação da Universidade Federal do Rio Grande do Norte (UFRN), envolvendo Machine Learning, processamento de sinais e análise de dados geofísicos.