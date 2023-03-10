import json

with open('dados.json', 'r') as f:
    data = json.load(f)

faturamento = [row['valor'] for row in data]

faturamento = [f for f in faturamento if f > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

media_mensal = sum(faturamento) / len(faturamento)

dias_acima_da_media = len([f for f in faturamento if f > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
