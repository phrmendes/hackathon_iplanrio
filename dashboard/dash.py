import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="LICITACAO.RIO",
    page_icon="📄",
    layout="wide"
)

# Título e descrição do Dashboard
st.title("📊 Dashboard de Licitações da Prefeitura do Rio")
st.markdown("""
Este dashboard apresenta uma visão geral das licitações realizadas no Licitação.rio.
Explore os gráficos e KPIs abaixo para insights rápidos.
""")

# Função para gerar dados fictícios
def gerar_dados_ficticios():
    np.random.seed(42)  # Reprodutibilidade
    orgaos = ['Prefeitura', 'Estado', 'Ministério', 'Autarquia', 'Empresa Pública']
    status = ['Em andamento', 'Concluído', 'Cancelado']
    categorias = ['Serviços', 'Obras', 'Equipamentos', 'Consultoria']

    dados = {
        'ID Licitação': np.arange(1, 101),
        'Órgão': np.random.choice(orgaos, 100),
        'Categoria': np.random.choice(categorias, 100),
        'Valor Estimado (R$)': np.round(np.random.uniform(50000, 1000000, 100), 2),
        'Status': np.random.choice(status, 100),
        'Data de Abertura': pd.date_range(start='2024-01-01', periods=100).to_list(),
    }
    return pd.DataFrame(dados)

# Gerar os dados
df = gerar_dados_ficticios()

# KPIs
st.subheader("🔍 KPIs")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Licitações", df['ID Licitação'].count())
col2.metric("Valor Total Estimado (R$)", f"R$ {df['Valor Estimado (R$)'].sum():,.2f}")
col3.metric("Licitações Concluídas", df[df['Status'] == 'Concluído'].shape[0])

# Gráfico de Distribuição por Órgão
st.subheader("📊 Distribuição de Licitações por Órgão")
df_orgaos = df['Órgão'].value_counts().reset_index()
df_orgaos.columns = ['Órgão', 'Número de Licitações']  # Renomear colunas para evitar confusão

fig1 = px.bar(
    df_orgaos,
    x='Órgão', y='Número de Licitações',
    labels={'Órgão': 'Órgão', 'Número de Licitações': 'Número de Licitações'},
    title='Quantidade de Licitações por Órgão'
)

st.plotly_chart(fig1, use_container_width=True)

# Gráfico de Valores Estimados por Categoria
st.subheader("💰 Valores Estimados por Categoria")
fig2 = px.pie(
    df, values='Valor Estimado (R$)', names='Categoria',
    title='Distribuição do Valor Estimado por Categoria'
)
st.plotly_chart(fig2, use_container_width=True)

# Filtro por Status e Data
st.subheader("📅 Filtro por Status e Período")
status_selecionado = st.selectbox("Selecione o Status:", df['Status'].unique())
data_inicial = st.date_input("Data Inicial", value=pd.to_datetime('2024-01-01'))
data_final = st.date_input("Data Final", value=pd.to_datetime('2024-12-31'))


# Garantir que a coluna 'Data de Abertura' está no formato datetime
df['Data de Abertura'] = pd.to_datetime(df['Data de Abertura'])

# Converter as datas selecionadas pelo usuário para datetime
data_inicial = pd.to_datetime(data_inicial)
data_final = pd.to_datetime(data_final)

# Aplicar os filtros com segurança
df_filtrado = df[
    (df['Status'] == status_selecionado) &
    (df['Data de Abertura'] >= data_inicial) &
    (df['Data de Abertura'] <= data_final)
]

# Mostrar tabela filtrada
st.subheader("📋 Licitações Filtradas")
st.dataframe(df_filtrado)

# Gráfico de Evolução Temporal
st.subheader("📈 Evolução Temporal das Licitações")
fig3 = px.line(
    df_filtrado, x='Data de Abertura', y='Valor Estimado (R$)',
    title='Evolução do Valor Estimado ao Longo do Tempo'
)
st.plotly_chart(fig3, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("🚀 Desenvolvido por DADOS IPLAN")
