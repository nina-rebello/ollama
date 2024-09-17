![Logo Preto](https://i.imgur.com/LyQ6ygf.png)

 # InsightWise - Comparação de Fluxos de Interação

Este projeto visa comparar fluxos de interação de usuários entre dados de referência e dados reais, gerando insights acionáveis a partir de discrepâncias encontradas. Usamos a biblioteca `streamlit` para criar uma interface gráfica onde os usuários podem visualizar gráficos, tabelas comparativas e insights detalhados sobre os dados de interação.

## Funcionalidades

- **Geração de Insights:** Compara os dados atuais de fluxo de interação com um fluxo de referência e gera insights sobre as discrepâncias encontradas, como diferenças de tempo e número de cliques em cada etapa.
- **Visualização de Dados:** Exibe gráficos visuais para facilitar a interpretação das diferenças entre o fluxo de referência e o fluxo atual.
  - Gráficos de barras comparativos
  - Gráficos de pizza mostrando a distribuição de tempo
  - Gráficos de dispersão mostrando a relação entre o número de cliques e o tempo gasto
  - Tabelas comparativas detalhadas
- **Análise Temporal e de Cliques:** Fornece uma análise visual e textual do tempo gasto e dos cliques em cada etapa do fluxo de interação.
- **Modelo de IA (Llama):** Integração com o modelo de IA Llama para fornecer insights verbais mais detalhados e complexos.

## Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit**
- **Pandas** para manipulação de dados
- **Matplotlib** para visualização de gráficos
- **Langchain** e **Ollama** para geração de insights detalhados através de IA


## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

Aqui está o texto formatado em Markdown para você copiar e colar no README do GitHub:

# Crie um ambiente virtual:

```bash
python -m venv env
```

## Ative o ambiente virtual:

### No Windows:
```bash
.\env\Scripts\activate
```

### No Linux/MacOS:
```bash
source env/bin/activate
```

## Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Usar

Coloque seus arquivos JSON no diretório principal do projeto. O JSON de referência deve ser nomeado como `cadastro_interacao.json` e o JSON atual como `cadastro.json`.

### Execute o projeto com Streamlit:

```bash
streamlit run streamlit.py
```

A interface será aberta automaticamente no seu navegador. Explore os insights gerados, gráficos e comparações diretamente pela interface.

## Estrutura do Projeto

```plaintext
├── cadastro.json                # Dados do fluxo atual
├── cadastro_interacao.json       # Dados de referência do fluxo
├── streamlit.py                  # Script principal da aplicação
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação do projeto
```

## Exemplo de Uso

### Insights Gerados

A partir da comparação dos fluxos, o sistema gera insights como:

- "Usuário gastou mais tempo na etapa 'Preencher dados pessoais' em comparação ao tempo de referência."
- "Número de cliques em 'Finalizar cadastro' foi maior do que o esperado."


