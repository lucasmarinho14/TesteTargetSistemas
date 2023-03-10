faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

valor_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

percentual_sp = (faturamento_sp / valor_total) * 100
percentual_rj = (faturamento_rj / valor_total) * 100
percentual_mg = (faturamento_mg / valor_total) * 100
percentual_es = (faturamento_es / valor_total) * 100
percentual_outros = (faturamento_outros / valor_total) * 100

print("Percentual de representação de cada estado no faturamento mensal da distribuidora:")
print("SP: {:.2f}%".format(percentual_sp))
print("RJ: {:.2f}%".format(percentual_rj))
print("MG: {:.2f}%".format(percentual_mg))
print("ES: {:.2f}%".format(percentual_es))
print("Outros: {:.2f}%".format(percentual_outros))
