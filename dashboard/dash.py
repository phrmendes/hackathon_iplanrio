import json
import sqlite3

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

st.set_page_config(
    page_title="Licitação.Rio - Dashboard",
    page_icon="./assets/favicon.ico",  # Caminho relativo para o favicon
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
        f'<h1 style="font-size: 48px; margin: 0;">{9}</h1>'
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
col5, col6, col7 = st.columns(3)

with col5:
    custom_metric("Mais de 1 Mês", etr_1_month_delay, "#FFFACD")  # Amarelo claro
with col6:
    custom_metric("Mais de 3 Meses", etr_3_months_delay, "#FFDAB9")  # Laranja claro
with col7:
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


st.subheader("📅 Filtro por Status, Período e Setor Demandante")


dados_etps = {
    "ID": [1, 2, 3, 4, 5],
    "Usuário": ["Alice", "Bruno", "Carlos", "Diana", "Eva"],
    "Número do Documento": [
        "IPL-PRO-2023/00016",
        "IPL-MEM-2024/00217",
        "IPL-PRO-2023/00441",
        "IPL-PRO-2024/00406",
        "IPL-MEM-2024/00616",
    ],
    "Tipo de Documento": [
        "Concluído",
        "Em andamento",
        "Cancelado",
        "Concluído",
        "Em andamento",
    ],
    "Órgão": ["SMS", "PRO", "MEM", "SMS", "PRO"],
    "Data de Criação": pd.to_datetime(
        ["2024-01-01", "2024-02-15", "2024-03-20", "2024-04-05", "2024-05-10"]
    ),
    "Data Prevista de Conclusão": pd.to_datetime(
        ["2024-06-01", "2024-07-15", "2024-08-20", "2024-09-05", "2024-10-10"]
    ),
}
df_adm_process = pd.DataFrame(dados_etps)

df_adm_process["Atraso (Dias)"] = (
    pd.to_datetime("2024-10-25") - df_adm_process["Data Prevista de Conclusão"]
).dt.days


if "reset" not in st.session_state:
    st.session_state.reset = False


status_options = ["Selecione...", "Concluído", "Em andamento", "Cancelado"]
selected_status = st.selectbox("Selecione o Status:", status_options, key="status")

setores = ["Selecione...", "SMS", "PRO", "MEM"]
selected_orgao = st.selectbox("Selecione o Setor Demandante:", setores, key="orgao")


# Inicializar valores na session_state, se não existirem
if "data_inicial" not in st.session_state:
    st.session_state.data_inicial = pd.to_datetime("2024-01-01")

if "data_final" not in st.session_state:
    st.session_state.data_final = pd.to_datetime("2024-12-31")

# Criando os inputs de data sem passar `value`
start_data = st.date_input("Data Inicial", key="data_inicial")
end_data = st.date_input("Data Final", key="data_final")


df_filtered = df_adm_process[
    (
        (selected_status == "Selecione...")
        | (df_adm_process["Tipo de Documento"] == selected_status)
    )
    & ((selected_orgao == "Selecione...") | (df_adm_process["Órgão"] == selected_orgao))
    & (df_adm_process["Data de Criação"] >= pd.to_datetime(start_data))
    & (df_adm_process["Data de Criação"] <= pd.to_datetime(end_data))
]


st.subheader("📋 ETPS Filtrados")
st.dataframe(df_filtered)

# Seção para fazer perguntas à LLM
st.header("🤖 Dúvidas sobre algum contrato? Fale com nossa IA!")

df_contratos = load_data(
    "SELECT organization || '-' || document_type || '-' || document_number AS Contratos FROM etp_admprocess LIMIT 5;"
)
st.write("Selecione um contrato:")

# Exibir a lista de contratos em um selectbox
selected_contract = st.selectbox(
    "Contratos", options=df_contratos["Contratos"].tolist()
)

# Separar o contrato selecionado em suas partes para consultar a tabela original
org, doc_type, doc_number = selected_contract.split("-")

# Buscar os dados completos da tabela etp_admprocess para o contrato selecionado
query = f"""
    SELECT *
    FROM etp_admprocess
    WHERE organization = '{org}'
      AND document_type = '{doc_type}'
      AND document_number = '{doc_number}';
"""
df_detailed = load_data(query)


# Carregar e exibir a tabela `etp_etp`
df_etp = load_data(f"SELECT * FROM etp_etp WHERE id = {df_detailed['id'].values[0]}")

# Converter o DataFrame `etp_etp` para JSON e exibir
etp_json = df_etp.to_json(orient="records", indent=2)


# Carregar e exibir a tabela `tr_tr`
df_tr = load_data(f"SELECT * FROM tr_tr WHERE id = {df_detailed['id'].values[0]}")

# Converter o DataFrame `tr_tr` para JSON e exibir
tr_json = df_tr.to_json(orient="records", indent=2)

# Verificar se um contrato foi selecionado
if selected_contract:
    # Carregar dados detalhados do contrato selecionado
    df_detailed = load_data(
        f"SELECT * FROM etp_admprocess WHERE organization || '-' || document_type || '-' || document_number = '{selected_contract}'"
    )

    # Carregar e converter dados da tabela `etp_etp` e `tr_tr` para JSON
    etp_json = load_data(
        f"SELECT justification, requesting_area, created_at, updated_at, status FROM etp_etp WHERE id = {df_detailed['id'].values[0]}"
    ).to_json(orient="records")
    tr_json = load_data(
        f"SELECT objective, justification, description, service_location, scheduled_date, created_at, updated_at, status FROM tr_tr WHERE id = {df_detailed['id'].values[0]}"
    ).to_json(orient="records")

    # Botão para enviar o contrato selecionado como prompt para a LLM
    if st.button("Enviar para LLM"):
        try:
            # Criar o prompt para a LLM
            prompt = (
                f"Resuma o contrato '{selected_contract}' com os dados dos json a seguir:\n\n"
                f"Tabela etp_etp: {etp_json}\n\n"
                f"Tabela tr_tr: {tr_json}\n\n"
                "Por favor, resuma essas informações em um único parágrafo."
            )

            # Indicar que a LLM está processando a requisição
            with st.spinner("Aguardando resposta da LLM..."):
                # Fazer a requisição GET para a LLM com o prompt como parâmetro
                response = requests.get(
                    "http://ollama-api:8000/ask", params={"prompt": prompt}
                )

            # Verificar e exibir a resposta
            if response.status_code == 200:
                st.write("Resposta da LLM:")
                st.write(response.json().get("response", "Sem resposta"))
            else:
                st.error(f"Erro {response.status_code} ao obter resposta da LLM.")
        except Exception as e:
            st.error(f"Erro ao fazer a requisição: {e}")

st.markdown(
    '<div class="footer">🚀 Desenvolvido por DADOS IPLAN</div>', unsafe_allow_html=True
)
