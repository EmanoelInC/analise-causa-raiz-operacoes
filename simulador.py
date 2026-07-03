import pandas as pd
import numpy as np

# 1. Criar dados simulados para demonstrar a engenharia do código sem expor dados reais
def criar_dados_ficticios():
    np.random.seed(42)
    vendedores = ['Vendedor A', 'Vendedor B', 'Vendedor C', 'Vendedor D']
    
    # Criar histórico de 3 meses de vendas
    dados = {
        'ID_Loja': [101] * 4,
        'Nome_Loja': ['Drogaria Rosário'] * 4,
        'Vendedor': vendedores,
        'Venda_Mes_1': np.random.randint(60000, 90000, 4),
        'Venda_Mes_2': np.random.randint(65000, 85000, 4),
        'Venda_Mes_3': np.random.randint(70000, 95000, 4),
        'CMV_Medio': [0.65, 0.64, 0.66, 0.63]
    }
    df = pd.DataFrame(dados)
    df.to_excel('dados_simulados.xlsx', index=False)
    print("✓ Arquivo 'dados_simulados.xlsx' criado com sucesso para o teste!")

# 2. Executar o motor de cálculo do Simulador de Metas
def processar_simulador_metas(percentual_crescimento=0.07):
    # Carregar dados
    df = pd.read_excel('dados_simulados.xlsx')
    
    # Calcular a Média Móvel dos últimos 3 meses
    df['Venda_Anterior_Media_3M'] = df[['Venda_Mes_1', 'Venda_Mes_2', 'Venda_Mes_3']].mean(axis=1)
    
    # Projetar a Meta Geral da Loja e Individuais
    df['Meta_Projetada'] = df['Venda_Anterior_Media_3M'] * (1 + percentual_crescimento)
    
    # Calcular Lucro Bruto Estimado com base no CMV de cada categoria/vendedor
    df['Lucro_Bruto_Estimado'] = df['Meta_Projetada'] * (1 - df['CMV_Medio'])
    
    # Salvar Racional de Rateio
    df.to_excel('Racional_Metas_Processado.xlsx', index=False)
    print("\n✓ Racional de Rateio e Projeção de Metas gerado com sucesso!")
    print(df[['Vendedor', 'Venda_Anterior_Media_3M', 'Meta_Projetada', 'Lucro_Bruto_Estimado']].round(2))

if __name__ == '__main__':
    criar_dados_ficticios()
    processar_simulador_metas(percentual_crescimento=0.07)