import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("data/db.sqlite3")
cursor = conn.cursor()

# Atualizar a tabela etp_etp para os IDs 2, 3, 4 e 5
cursor.execute("""
    UPDATE etp_etp
    SET 
        justification = 'A solicitação é necessária para atender às demandas de serviços essenciais na área.',
        requesting_area = 'Departamento de Logística',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Em Andamento'
    WHERE id = 2
""")

cursor.execute("""
    UPDATE etp_etp
    SET 
        justification = 'Revisão do projeto de infraestrutura necessário para o crescimento da empresa.',
        requesting_area = 'Departamento de Engenharia',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Em Análise'
    WHERE id = 3
""")

cursor.execute("""
    UPDATE etp_etp
    SET 
        justification = 'Análise de viabilidade econômica para novo produto.',
        requesting_area = 'Departamento de Pesquisa e Desenvolvimento',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Aguardando Aprovação'
    WHERE id = 4
""")

cursor.execute("""
    UPDATE etp_etp
    SET 
        justification = 'Contratação de serviços de segurança para proteção de ativos.',
        requesting_area = 'Departamento de Segurança',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Pendente'
    WHERE id = 5
""")

# Atualizar a tabela tr_tr para os IDs 2, 3, 4 e 5
cursor.execute("""
    UPDATE tr_tr
    SET 
        objective = 'Contratação de serviços de consultoria para otimização de processos',
        justification = 'Justificativa baseada na necessidade de melhoria contínua da eficiência operacional.',
        description = 'Serviços de consultoria incluirão análise de processos e recomendações para melhorias.',
        service_location = 'Sede Administrativa',
        scheduled_date = '2024-11-15',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Em Andamento'
    WHERE id = 2
""")

cursor.execute("""
    UPDATE tr_tr
    SET 
        objective = 'Implantação de sistema de gestão de projetos',
        justification = 'Melhoria na eficiência de gerenciamento de projetos internos.',
        description = 'O sistema permitirá melhor acompanhamento e gestão de recursos e prazos.',
        service_location = 'Sede Administrativa',
        scheduled_date = '2024-12-01',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Em Planejamento'
    WHERE id = 3
""")

cursor.execute("""
    UPDATE tr_tr
    SET 
        objective = 'Realização de treinamento para equipe de vendas',
        justification = 'Necessidade de aprimorar as técnicas de vendas da equipe.',
        description = 'O treinamento abrangerá técnicas de negociação e atendimento ao cliente.',
        service_location = 'Centro de Treinamento',
        scheduled_date = '2024-11-20',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Agendado'
    WHERE id = 4
""")

cursor.execute("""
    UPDATE tr_tr
    SET 
        objective = 'Contratação de serviços de limpeza para nova sede',
        justification = 'Preparação da nova sede para recebimento de colaboradores.',
        description = 'Serviços de limpeza incluem higienização profunda e organização do espaço.',
        service_location = 'Nova Sede',
        scheduled_date = '2024-11-30',
        updated_at = CURRENT_TIMESTAMP,
        status = 'Pendente'
    WHERE id = 5
""")

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
