import logging
import colorlog
import csv
from datetime import datetime


# ===============================
# CONFIGURAÇÃO DO LOGGER
# ===============================
def setup_logger():
    logger = logging.getLogger("ncm_validator")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
            log_colors={
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
            },
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# ===============================
# VALIDADOR DE NCM
# ===============================
def validar_ncm(ncm):
    if not ncm:
        return "SEM NCM"

    ncm_str = str(ncm).strip()

    if not ncm_str.isdigit():
        return "NCM INVÁLIDO"

    if len(ncm_str) != 8:
        return "NCM INVÁLIDO"

    return "OK"


# ===============================
# EXPORTAR CSV
# ===============================
def exportar_csv(resultados):
    nome_arquivo = "(resultados_csv, resultado_ncm.csv)"

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["NCM", "Status"])

        for linha in resultados:
            writer.writerow(linha)

    print(f"\n📁 Arquivo '{nome_arquivo}' gerado com sucesso!")


# ===============================
# FUNÇÃO PRINCIPAL
# ===============================
def main():
    logger = setup_logger()

    logger.info("Iniciando validação de NCMs...")

    lista_ncms = [
        "12345678",
        "87654321",
        "87654321",
        "87654321",
        "87654321",
        "87654321",
        "87654321",
    ]

    total = 0
    validos = 0
    invalidos = 0

    resultados_csv = []

    print("\n" + "=" * 50)
    print("RESULTADO DA VALIDAÇÃO")
    print("=" * 50)

    for ncm in lista_ncms:
        total += 1
        status = validar_ncm(ncm)

        resultados_csv.append([ncm, status])

        if status == "OK":
            validos += 1
            logger.info(f"NCM {ncm} válido.")
        else:
            invalidos += 1
            logger.warning(f"NCM {ncm} → {status}")

        print(f"NCM: {str(ncm):<12} | Status: {status}")

    print("=" * 50)
    print(f"Total analisados : {total}")
    print(f"Válidos          : {validos}")
    print(f"Inválidos        : {invalidos}")
    print("=" * 50)

    exportar_csv(resultados_csv)

    logger.info("Validação finalizada.")


if __name__ == "__main__":
    main()

