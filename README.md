# Simulador Inteligente de Metas e Análise de Rentabilidade 💊

Este repositório contém uma solução automatizada em Python desenvolvida para substituir processos manuais de estipulação e rateio de metas em redes do varejo farmacêutico.

## 📈 Problema de Negócio
Gerenciar e desdobrar metas de vendas manualmente utilizando planilhas estáticas frequentemente gera distorções em indicadores críticos de rentabilidade (como CMV e Margem Bruta), além de lentidão no repasse de metas MoM (Mês sobre Mês) e YTD (Acumulado do Ano).

## 🛠️ Solução Desenvolvida
O script em Python (`simulador.py`) atua como o motor de cálculo:
1. Consolida o histórico de vendas e calcula uma **Média Móvel ponderada de 3 meses**.
2. Aplica algoritmos de crescimento customizáveis de forma preditiva.
3. Desenha o **Racional de Rateio de Premiação por Vendedor** de forma proporcional e justa.
4. Calcula a projeção de **Lucro Bruto** cruzando as metas com o CMV estimado.

## 💻 Tecnologias
* Python 3
* Pandas & NumPy (Engenharia de Recursos e Processamento de Vetores)
* Excel OpenPyXL