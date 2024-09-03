import json

with open("projetosPessoais/testeEstágio2/faturamentoDiario.json", 'r') as file:
    faturamento_diario = json.load(file)

menor_faturamento = float('inf')
maior_faturamento = float('-inf')
soma_faturamento = 0
dias_com_faturamento = 0

for dia in faturamento_diario:
    faturamento = dia['valor']
    
    if faturamento > 0:
        if faturamento < menor_faturamento:
            menor_faturamento = faturamento
        if faturamento > maior_faturamento:
            maior_faturamento = faturamento
        
        soma_faturamento += faturamento
        dias_com_faturamento += 1

media_mensal = soma_faturamento / dias_com_faturamento if dias_com_faturamento > 0 else 0

dias_acima_da_media = sum(1 for dia in faturamento_diario if dia['valor'] > media_mensal)

print("Menor valor de faturamento ocorrido em um dia do mês:", menor_faturamento)
print("Maior valor de faturamento ocorrido em um dia do mês:", maior_faturamento)
print("Número de dias com faturamento diário superior à média mensal:", dias_acima_da_media)
