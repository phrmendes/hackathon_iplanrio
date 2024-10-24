import pandas as pd

# Carregar o CSV
df = pd.read_csv('data/trs.csv')

# Selecionar apenas as colunas necessárias
columns = ['Processo Instrutivo',
           'Objeto',
           'Situação',
           'Estimativa Gasto em 2024',
           'Emissão da ETP, do TR e convocação do GT',
           'Entrega dos produtos/ incio dos serviços']
df = df[columns]

# Filtrar registros onde 'Emissão da ETP, do TR e convocação do GT' e 'Entrega dos produtos/ incio dos serviços' não são "-"
df = df[df['Emissão da ETP, do TR e convocação do GT'] != '-']
df = df[df['Entrega dos produtos/ incio dos serviços'] != '-']

# Remover registros com NaN nessas colunas
df = df.dropna(subset=['Emissão da ETP, do TR e convocação do GT', 'Entrega dos produtos/ incio dos serviços'])


# Criar um dicionário para mapear cada objeto ao cluster correspondente
cluster_map = {
    'Aquisação de equipamentos audivisuais': 'Aquisição e Fornecimento de Equipamentos e Materiais',
    'Remoção cabeamento e materiaIs das salas do Teleporto': 'Serviços de Mudança e Reforma',
    'Empresa reforma  salas Teleporto e sala 307': 'Serviços de Mudança e Reforma',
    'As Caixas de papelão serão fornecidas como empréstimo pela empresa de mudança.  As caixas tipo BOX a a fita autoadesiva serão adquridos por SDP.': 'Aquisição e Fornecimento de Equipamentos e Materiais',
    'Empresa mudança': 'Serviços de Mudança e Reforma',
    'Gerenciamento de Impressão ASG\nContrato terminará em 08/05/24': 'Gerenciamento e Consultoria',
    'Eletrodomésticos 220V': 'Aquisição e Fornecimento de Equipamentos e Materiais',
    'Projeto e implantação comunicação visual CCN': 'Serviços de Comunicação e Tecnologia',
    'Extintores de Incêndio para a nova sede': 'Segurança',
    'Acessórios de higienie': 'Aquisição e Fornecimento de Equipamentos e Materiais',
    'Estantes em aço': 'Aquisição e Fornecimento de Equipamentos e Materiais',
    'Mentoria em Medição de Software': 'Gerenciamento e Consultoria',
    'Link de Internet de 200M com serviço de Firewall para o Palácio Oeste': 'Serviços de Comunicação e Tecnologia',
    'Manutenção Extintores do Anexo': 'Segurança'
}

# Aplicar o mapeamento para criar a coluna de clusters
df['Cluster'] = df['Objeto'].map(cluster_map)

# Converter as colunas de data para o tipo datetime
df['Emissão da ETP, do TR e convocação do GT'] = pd.to_datetime(df['Emissão da ETP, do TR e convocação do GT'])
df['Entrega dos produtos/ incio dos serviços'] = pd.to_datetime(df['Entrega dos produtos/ incio dos serviços'])


# Calcular a diferença de dias entre as duas colunas de data
df['Diferença em dias'] = (df['Entrega dos produtos/ incio dos serviços'] - df['Emissão da ETP, do TR e convocação do GT']).dt.days

# Calcular a média da diferença de dias para cada cluster
media_por_cluster = df.groupby('Cluster')['Diferença em dias'].mean()

# Exibir o resultado
print(media_por_cluster)