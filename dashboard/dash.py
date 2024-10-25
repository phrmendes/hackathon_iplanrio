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
col1, col2, col3, col4 = st.columns(4)

# KPI 1: ETP total
with col1:
    etp_total = df_adm_process.shape[0]
    st.markdown(
        '<div class="kpi-box">'
        "<h3> Total de Estudos Técnicos </h3>"
        f'<h1 style="font-size: 48px; margin: 0;">{9}</h1>'
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
        f'<h1 style="font-size: 48px; margin: 0;">{10}</h1>'
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
# #KPI 3: ETPS concluded
etps_concluded = 3
# TODO: Como identificar ETPS concluídas?
# licitations_concluded = df_adm_process[sf_adm_process["document_type"] == "Concluído"].shape[0]
with col3:
    st.markdown(
        '<div class="kpi-box">'
        "<h3> Estudos Técnicos Concluídos </h3>"
        f'<h1 style="font-size: 48px; margin: 0;">{etps_concluded}</h1>'
        "</div>",
        unsafe_allow_html=True,
    )

# KPI4: tERMS concluded
trs_concluded = 2
with col4:
    st.markdown(
        '<div class="kpi-box">'
        "<h3> Termos de Referência Concluídos </h3>"
        f'<h1 style="font-size: 48px; margin: 0;">{trs_concluded}</h1>'
        "</div>",
        unsafe_allow_html=True,
    )

# Exemplo de dados fictícios para cada categoria
data = {
    "Organização": ["SMS", "PRO", "MEM"],
    "Número de Licitações": [50, 75, 30],  # Valores diferentes para cada categoria
}

# Criar um DataFrame a partir dos dados
df_org = pd.DataFrame(data)

# Definir a nova paleta de cores clara
custom_colors = [
    "#ADD8E6",
    "#ade6d8",
    "#adbce6",
]  # Azul claro, amarelo dourado, rosa choque


# Gerar o gráfico de barras com a nova paleta de cores clara
# Rename Organization to Orgão
df_org = df_org.rename(columns={"Organização": "Órgão"})

fig1 = px.bar(
    df_org,
    x="Órgão",
    y="Número de Licitações",
    title="Distribuição de Licitações por Orgão",
    color="Órgão",  # Use a coluna para colorir
    color_discrete_sequence=custom_colors,  # Aplicar a nova paleta de cores claras
)
st.plotly_chart(fig1, use_container_width=True)


# Search products and average price
# Função para criar uma métrica com label maior usando HTML e CSS


def custom_metric(label, value, color):
    st.markdown(
        f"""
        <div style="text-align: center; background-color: {color}; padding: 10px; border-radius: 10px;">
            <p style="font-size:24px; font-weight: bold;">{label}</p>
            <p style="font-size:48px; margin: -10px 0; font-weight: bold;">{value}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Layout para mostrar os processos com mais de 1, 3 e 6 meses de atraso
st.subheader("⏰ Tempo de vida Estudos Técnicos e Termos de Referência")

# Dados fictícios para ETPs (Estudos Técnicos)
etp_1_month_delay = 25
etp_3_months_delay = 15
etp_6_months_delay = 8

# Dados fictícios para ETRs (Termos de Referência)
etr_1_month_delay = 18
etr_3_months_delay = 12
etr_6_months_delay = 5

# Layout das caixas para ETPs
st.markdown("#### Estudos Técnicos com Atraso")
col1, col2, col3 = st.columns(3)

with col1:
    custom_metric("Mais de 1 Mês", etp_1_month_delay, "#FFFACD")  # Amarelo claro
with col2:
    custom_metric("Mais de 3 Meses", etp_3_months_delay, "#FFDAB9")  # Laranja claro
with col3:
    custom_metric("Mais de 6 Meses", etp_6_months_delay, "#F08080")  # Vermelho claro

st.markdown("#")


# Lista dos ETPs mais atrasados com seus tempos em dias
st.markdown("#### Maiores Atrasos")

# Dados fictícios: Lista de ETPs mais atrasados com seus tempos em dias
etp_delay_data = [
    {"ETP": "IPL-PRO-2023/00016", "Dias de Atraso": 189},
    {"ETP": "IPL-MEM-2024/00217", "Dias de Atraso": 131},
    {"ETP": "IPL-PRO-2023/00441", "Dias de Atraso": 124},
    {"ETP": "IPL-PRO-2024/00406", "Dias de Atraso": 85},
    {"ETP": "IPL-MEM-2024/00616", "Dias de Atraso": 61},
]

# Layout horizontal para a lista
st.markdown(
    "<div style='display: flex; justify-content: space-between;'>"
    + "".join(
        [
            f"<div style='margin-right: 20px;'>"
            f"<strong>{item['ETP']}</strong><br>"
            f"{item['Dias de Atraso']} dias"
            "</div>"
            for item in etp_delay_data
        ]
    )
    + "</div>",
    unsafe_allow_html=True,
)
# Separador visual
st.markdown("---")

# Layout das caixas para ETRs
st.markdown("#### Termos de Referência com Atraso")
col4, col5, col6 = st.columns(3)

with col4:
    custom_metric("Mais de 1 Mês", etr_1_month_delay, "#FFFACD")  # Amarelo claro
with col5:
    custom_metric("Mais de 3 Meses", etr_3_months_delay, "#FFDAB9")  # Laranja claro
with col6:
    custom_metric("Mais de 6 Meses", etr_6_months_delay, "#F08080")  # Vermelho claro

st.markdown("#")


# Lista dos ETPs mais atrasados com seus tempos em dias
st.markdown("#### Maiores Atrasos")

etp_delay_data = [
    {"ETP": "IPL-MEM-2023/00019", "Dias de Atraso": 192},
    {"ETP": "IPL-PRO-2024/00220", "Dias de Atraso": 137},
    {"ETP": "IPL-MEM-2023/00450", "Dias de Atraso": 128},
    {"ETP": "IPL-PRO-2024/00408", "Dias de Atraso": 92},
    {"ETP": "IPL-MEM-2024/00620", "Dias de Atraso": 65},
]

# Layout horizontal para a lista
st.markdown(
    "<div style='display: flex; justify-content: space-between;'>"
    + "".join(
        [
            f"<div style='margin-right: 20px;'>"
            f"<strong>{item['ETP']}</strong><br>"
            f"{item['Dias de Atraso']} dias"
            "</div>"
            for item in etp_delay_data
        ]
    )
    + "</div>",
    unsafe_allow_html=True,
)
# Separador visual
st.markdown("---")

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

st.markdown(
    '<div class="footer">🚀 Desenvolvido por DADOS IPLAN</div>', unsafe_allow_html=True
)
