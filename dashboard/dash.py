import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="LICITACAO.RIO",
    page_icon="📄",
    layout="wide",
)


def load_css(path):
    """Load external CSS"""
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("src/styles.css")


def load_data(query):
    """Load data from SQLite database"""
    conn = sqlite3.connect("data/db.sqlite3")
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


df_adm_process = load_data("SELECT * FROM etp_admprocess")
df_market = load_data("SELECT * FROM etp_marketresearch")
df_contract = load_data("SELECT * FROM etp_contractestimate")
df_installment = load_data("SELECT * FROM etp_installment")

# KPIs styled
col1, col2, col3 = st.columns(3)

# KPI 1: ETP total
with col1:
    etp_total = df_adm_process.shape[0]
    st.markdown(
        '<div class="kpi-box">'
        "<h3> Total de Estudos Técnicos </h3>"
        f'<h1 style="font-size: 48px; margin: 0;">{etp_total}</h1>'
        "</div>",
        unsafe_allow_html=True,
    )

# KPI 2: TR total
# TODO: COMO IDENTIFICAR TRs?
with col2:
    tr_total = df_adm_process.shape[0]
    st.markdown(
        '<div class="kpi-box">'
        "<h3> Total de Termos de Referência </h3>"
        f'<h1 style="font-size: 48px; margin: 0;">{tr_total}</h1>'
        "</div>",
        unsafe_allow_html=True,
    )


# with col2:
#     st.markdown(
#         '<div class="kpi-box">'
#         "<h3> Valor Total Estimado (R$) </h3>"
#         f'<h1 style="font-size: 48px; margin: 0;">{formatted_value}</h1>'
#         "</div>",
#         unsafe_allow_html=True,
#     )

# Format the value as Brazilian currency
estimated_total_value = df_contract["unit_price"].mul(df_contract["quantity"]).sum()
formatted_value = (
    f"R$ {estimated_total_value:,.2f}".replace(",", "X")
    .replace(".", ",")
    .replace("X", ".")
)
# #KPI 3: Licitations concluded
# TODO: Como identificar ETPS concluídas?
# licitations_concluded = df_adm_process[sf_adm_process["document_type"] == "Concluído"].shape[0]
with col3:
    st.markdown(
        '<div class="kpi-box">'
        "<h3> Valor Total Estimado (R$) </h3>"
        f'<h1 style="font-size: 48px; margin: 0;">{formatted_value}</h1>'
        "</div>",
        unsafe_allow_html=True,
    )

# Distribution of organizations
st.subheader("📊 Distribuição de Licitações por Setor")
df_org = df_adm_process["organization"].value_counts().reset_index()
df_org.columns = ["Organização", "Número de Licitações"]

fig1 = px.bar(
    df_org,
    x="Organização",
    y="Número de Licitações",
    title="Distribuição de Licitações por Organização",
)
st.plotly_chart(fig1, use_container_width=True)


# Search products and average price
st.subheader("💰 Produtos Pesquisados e Valor Médio")
fig2 = px.scatter(
    df_market,
    x="product",
    y="unit_price",
    size="unit_price",
    color="unit_price_currency",
    title="Produtos Pesquisados - Valor Médio",
)
st.plotly_chart(fig2, use_container_width=True)


# Filtered table by status and period
st.subheader("📅 Filtro por Status e Período")

status_options = ["Concluído", "Em andamento", "Cancelado"]
selected_status = st.selectbox("Selecione o Status:", status_options)

# Inputs of data
start_data = st.date_input("Data Inicial", value=pd.to_datetime("2024-01-01").date())
end_data = st.date_input("Data Final", value=pd.to_datetime("2024-12-31").date())

# data conversion
start_data = pd.to_datetime(start_data)
end_data = pd.to_datetime(end_data)
df_adm_process["year"] = pd.to_datetime(df_adm_process["year"], format="%Y")

df_filtered = df_adm_process[
    (df_adm_process["document_type"] == selected_status)
    & (df_adm_process["year"] >= start_data)
    & (df_adm_process["year"] <= end_data)
]

df_filtered = df_filtered.rename(
    columns={
        "id": "ID",
        "user": "Usuário",
        "document_number": "Número do Documento",
        "document_type": "Tipo de Documento",
        "user_id": "ID do Usuário",
        "organization": "Organização",
        "year": "Ano",
    }
)

st.subheader("📋 ETPS Filtradas")
st.dataframe(df_filtered)

# Evolution of biddings
df_grouped = (
    df_filtered.groupby(df_filtered["Ano"].dt.to_period("M"))
    .size()
    .reset_index(name="Total")
)
df_grouped["Ano"] = df_grouped["Ano"].astype(str)

fig3 = px.line(
    df_grouped,
    x="Ano",
    y="Total",
    title="Evolução dos ETP/TRs",
    labels={"Ano": "Mês-Ano", "Total": "Total de Licitações"},
)
fig3.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig3, use_container_width=True)

st.markdown(
    '<div class="footer">🚀 Desenvolvido por DADOS IPLAN</div>', unsafe_allow_html=True
)
