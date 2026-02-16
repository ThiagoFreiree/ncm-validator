import csv


def exportar_csv(resultados, nome_arquivo):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["NCM", "Status"])

        for linha in resultados:
            writer.writerow(linha)