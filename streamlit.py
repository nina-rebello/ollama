import pandas as pd
import json
import streamlit as st
import matplotlib.pyplot as plt
from langchain_community.llms import Ollama

# Função para ler o arquivo JSON
def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Função para comparar os JSONs e gerar insights
def compare_json(current_json, reference_json):
    insights = []
    df_current = pd.DataFrame(current_json['flow'])
    df_reference = pd.DataFrame(reference_json['flow'])

    # Verificar diferenças no número de etapas
    if len(df_current) != len(df_reference):
        insights.append(f"Número de etapas diferentes: {len(df_current)} no fluxo atual, {len(df_reference)} no de referência.")

    # Comparar cada etapa
    for i, row in df_current.iterrows():
        if i < len(df_reference):
            ref_row = df_reference.iloc[i]

            if row['duration_seconds'] > ref_row['duration_seconds']:
                insights.append(f"Usuário gastou {row['duration_seconds']}s em '{row['step']}', mais que o tempo de referência de {ref_row['duration_seconds']}s.")
            elif row['duration_seconds'] < ref_row['duration_seconds']:
                insights.append(f"Usuário gastou {row['duration_seconds']}s em '{row['step']}', menos que o tempo de referência de {ref_row['duration_seconds']}s.")

            if row['clicks'] != ref_row['clicks']:
                insights.append(f"Usuário clicou {row['clicks']} vezes, diferente dos {ref_row['clicks']} esperados.")
        else:
            insights.append(f"Não há etapa correspondente no fluxo de referência.")
    
    return insights, df_current, df_reference

# Função para criar gráficos
def plot_comparison(df_current, df_reference):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_current['step'], df_current['duration_seconds'], color='blue', label='Atual')
    ax.bar(df_reference['step'], df_reference['duration_seconds'], color='orange', alpha=0.6, label='Referência')
    ax.set_ylabel('Duração (segundos)')
    ax.set_title('Comparação de Tempo por Etapa')
    ax.legend()
    return fig

def plot_pie_chart(df_current):
    fig, ax = plt.subplots()
    ax.pie(df_current['duration_seconds'], labels=df_current['step'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Para manter o gráfico como um círculo
    plt.title('Distribuição de Tempo por Etapa')
    return fig


def plot_scatter(df_current):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df_current['clicks'], df_current['duration_seconds'], color='purple')
    ax.set_xlabel('Número de Cliques')
    ax.set_ylabel('Duração (segundos)')
    ax.set_title('Relação entre Cliques e Tempo Gasto')
    return fig

def create_comparison_table(df_current, df_reference):
    comparison = pd.DataFrame({
        'Etapa': df_current['step'],
        'Duração Atual (s)': df_current['duration_seconds'],
        'Duração Referência (s)': df_reference['duration_seconds'],
        'Cliques Atual': df_current['clicks'],
        'Cliques Referência': df_reference['clicks']
    })
    return comparison

def plot_line_comparison(df_current, df_reference):
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(df_current['step'], df_current['duration_seconds'], marker='o', label='Atual', color='blue')
    ax.plot(df_reference['step'], df_reference['duration_seconds'], marker='o', label='Referência', color='orange')
    ax.set_ylabel('Duração (segundos)')
    ax.set_title('Comparação de Duração ao Longo das Etapas')
    ax.legend()
    return fig

# Função para gerar insights detalhados usando o modelo Ollama
def generate_detailed_insights(current_json, reference_json):
    model = Ollama(model="llama3")  # Configurar o modelo que você está usando
    prompt = (
    "Compare os seguintes dados JSON e forneça insights detalhados. "
    "Utilize os dados de referência para destacar discrepâncias e sugerir melhorias.\n\n"
    "Dados de Referência:\n"
    f"{json.dumps(reference_json, indent=2)}\n\n"
    "Dados Atuais:\n"
    f"{json.dumps(current_json, indent=2)}\n"
    "Forneça uma análise detalhada e insights acionáveis."
    "Responda em português"
    )
    response = model.invoke(prompt)
    return response.strip()

# Ler JSONs
reference_json = read_json('cadastro_interacao.json')
current_json = read_json('cadastro.json')

# Gerar insights
insights, df_current, df_reference = compare_json(current_json, reference_json)

# Gerar insights detalhados
detailed_insights = generate_detailed_insights(current_json, reference_json)

# Interface do Streamlit
st.title('Dashboard de Comparação de Interações')
st.write('Comparação entre fluxo de referência e fluxo atual.')

# Exibir insights
st.subheader('Insights Gerados')
for insight in insights:
    st.write(f"- {insight}")

# Exibir insights detalhados do modelo Ollama
st.subheader('Insights Detalhados do Modelo Ollama')
st.write(detailed_insights)

# Exibir gráficos

st.subheader('Comparação Visual de Duração')
fig = plot_comparison(df_current, df_reference)
st.pyplot(fig)

st.subheader('Distribuição de Tempo por Etapa (Atual)')
fig_pie = plot_pie_chart(df_current)
st.pyplot(fig_pie)

st.subheader('Análise Temporal das Durações por Etapa')
fig_line = plot_line_comparison(pd.DataFrame(current_json['flow']), pd.DataFrame(reference_json['flow']))
st.pyplot(fig_line)

st.subheader('Relação entre Cliques e Tempo Gasto')
fig_scatter = plot_scatter(df_current)
st.pyplot(fig_scatter)

st.subheader('Tabela Comparativa')
comparison_table = create_comparison_table(df_current, df_reference)
st.dataframe(comparison_table)
