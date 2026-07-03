import pandas as pd
import matplotlib.pyplot as plt

def gerar_analise_pareto():
    print("=== Executando Análise Estatística de Ocorrências (Pareto) ===")
    
    # Dados reais agregados baseados no histórico de ocorrências de rua e devoluções
    dados_ocorrencias = {
        'Motivo_Devolucao': ['Endereço Não Localizado', 'Cliente Recusou', 'Avaria de Transporte', 'Divergência de Preço', 'Erro de Carregamento'],
        'Quantidade': [63, 28, 12, 8, 4]
    }
    
    df = pd.DataFrame(dados_ocorrencias)
    df = df.sort_values(by='Quantidade', ascending=False)
    
    # Cálculos para o Princípio de Pareto (80/20)
    df['Percentual'] = (df['Quantidade'] / df['Quantidade'].sum()) * 100
    df['Percentual_Acumulado'] = df['Percentual'].cumsum()
    
    print("\n -> Matriz de Dispersão de Perdas:")
    print(df.round(2).to_string(index=False))
    
    # Salvando indicador de eficiência
    df.to_csv('matriz_causa_raiz.csv', index=False)

if __name__ == "__main__":
    gerar_analise_pareto()
