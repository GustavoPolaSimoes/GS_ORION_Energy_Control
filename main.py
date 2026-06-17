import random
import csv
from datetime import datetime

AREA_PAINEIS_M2 = 6.0
CAPACIDADE_BATERIA_WH = 5000


def gerar_telemetria():
    return {
        "temperatura_c": random.randint(18, 42),
        "comunicacao_percent": random.randint(40, 100),
        "bateria_percent": random.randint(10, 100),
        "irradiancia_solar_w_m2": random.randint(150, 950),
        "eficiencia_painel_percent": random.randint(45, 92),
        "consumo_suporte_vida_w": random.randint(700, 1000),
        "consumo_comunicacao_w": random.randint(250, 550),
        "consumo_pesquisa_w": random.randint(200, 700),
        "consumo_controle_termico_w": random.randint(300, 850),
    }


def calcular_energia(dados):
    eficiencia = dados["eficiencia_painel_percent"] / 100

    potencia_solar_w = dados["irradiancia_solar_w_m2"] * AREA_PAINEIS_M2 * eficiencia

    consumo_total_w = (
        dados["consumo_suporte_vida_w"]
        + dados["consumo_comunicacao_w"]
        + dados["consumo_pesquisa_w"]
        + dados["consumo_controle_termico_w"]
    )

    saldo_energetico_w = potencia_solar_w - consumo_total_w

    energia_bateria_wh = CAPACIDADE_BATERIA_WH * (dados["bateria_percent"] / 100)

    if consumo_total_w > 0:
        autonomia_horas = energia_bateria_wh / consumo_total_w
    else:
        autonomia_horas = 0

    percentual_renovavel = min((potencia_solar_w / consumo_total_w) * 100, 100)

    return {
        "potencia_solar_w": round(potencia_solar_w, 2),
        "consumo_total_w": consumo_total_w,
        "saldo_energetico_w": round(saldo_energetico_w, 2),
        "energia_bateria_wh": round(energia_bateria_wh, 2),
        "autonomia_horas": round(autonomia_horas, 2),
        "percentual_renovavel": round(percentual_renovavel, 2),
    }


def gerar_alertas(dados, energia):
    alertas = []

    if dados["temperatura_c"] > 35:
        alertas.append("Temperatura elevada no sistema operacional.")

    if dados["comunicacao_percent"] < 60:
        alertas.append("Comunicação instável com a base de controle.")

    if dados["bateria_percent"] < 25:
        alertas.append("Bateria em nível crítico.")

    if energia["saldo_energetico_w"] < 0:
        alertas.append("Consumo maior que a geração de energia solar.")

    if energia["autonomia_horas"] < 2:
        alertas.append("Autonomia energética inferior a 2 horas.")

    if dados["eficiencia_painel_percent"] < 55:
        alertas.append("Baixa eficiência dos painéis solares.")

    return alertas


def classificar_status(alertas):
    qtd = len(alertas)

    if qtd == 0:
        return "NORMAL"
    elif qtd <= 2:
        return "ATENÇÃO"
    elif qtd <= 4:
        return "CRÍTICO"
    else:
        return "EMERGÊNCIA"


def recomendar_acao(dados, energia, status):
    recomendacoes = []

    if energia["saldo_energetico_w"] < 0:
        recomendacoes.append("Ativar modo de economia de energia.")
        recomendacoes.append("Reduzir consumo dos módulos não essenciais.")

    if dados["bateria_percent"] < 25:
        recomendacoes.append("Priorizar suporte à vida, comunicação e controle térmico.")

    if dados["eficiencia_painel_percent"] < 55:
        recomendacoes.append("Reorientar painéis solares para melhorar captação.")

    if dados["comunicacao_percent"] < 60:
        recomendacoes.append("Reduzir transmissão de dados não críticos e tentar restabelecer sinal.")

    if dados["temperatura_c"] > 35:
        recomendacoes.append("Aumentar prioridade do controle térmico.")

    if status == "NORMAL":
        recomendacoes.append("Manter operação padrão e continuar monitoramento.")

    return recomendacoes


def exibir_resultado(dados, energia, alertas, status, recomendacoes):
    print("\n" + "=" * 55)
    print("AURORA ENERGY CONTROL")
    print("Sistema de Monitoramento Energético Espacial")
    print("=" * 55)

    print(f"\nSTATUS GERAL: {status}")

    print("\n--- TELEMETRIA DA MISSÃO ---")
    print(f"Temperatura: {dados['temperatura_c']} °C")
    print(f"Comunicação: {dados['comunicacao_percent']}%")
    print(f"Bateria: {dados['bateria_percent']}%")
    print(f"Irradiância solar: {dados['irradiancia_solar_w_m2']} W/m²")
    print(f"Eficiência dos painéis: {dados['eficiencia_painel_percent']}%")

    print("\n--- ANÁLISE ENERGÉTICA ---")
    print(f"Potência solar gerada: {energia['potencia_solar_w']} W")
    print(f"Consumo total dos módulos: {energia['consumo_total_w']} W")
    print(f"Saldo energético: {energia['saldo_energetico_w']} W")
    print(f"Autonomia estimada: {energia['autonomia_horas']} horas")
    print(f"Aproveitamento renovável: {energia['percentual_renovavel']}%")

    print("\n--- ALERTAS AUTOMÁTICOS ---")
    if alertas:
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("- Nenhum alerta crítico identificado.")

    print("\n--- TOMADA DE DECISÃO AUTOMÁTICA ---")
    for rec in recomendacoes:
        print(f"- {rec}")

    print("\n" + "=" * 55)


def salvar_historico(dados, energia, status, alertas):
    nome_arquivo = "historico_simulacao.csv"

    linha = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": status,
        "temperatura_c": dados["temperatura_c"],
        "comunicacao_percent": dados["comunicacao_percent"],
        "bateria_percent": dados["bateria_percent"],
        "irradiancia_solar_w_m2": dados["irradiancia_solar_w_m2"],
        "eficiencia_painel_percent": dados["eficiencia_painel_percent"],
        "potencia_solar_w": energia["potencia_solar_w"],
        "consumo_total_w": energia["consumo_total_w"],
        "saldo_energetico_w": energia["saldo_energetico_w"],
        "autonomia_horas": energia["autonomia_horas"],
        "percentual_renovavel": energia["percentual_renovavel"],
        "qtd_alertas": len(alertas),
    }

    try:
        with open(nome_arquivo, "x", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=linha.keys())
            escritor.writeheader()
            escritor.writerow(linha)
    except FileExistsError:
        with open(nome_arquivo, "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=linha.keys())
            escritor.writerow(linha)


def main():
    dados = gerar_telemetria()
    energia = calcular_energia(dados)
    alertas = gerar_alertas(dados, energia)
    status = classificar_status(alertas)
    recomendacoes = recomendar_acao(dados, energia, status)

    exibir_resultado(dados, energia, alertas, status, recomendacoes)
    salvar_historico(dados, energia, status, alertas)


if __name__ == "__main__":
    main()