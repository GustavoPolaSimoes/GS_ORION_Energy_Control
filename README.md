# AURORA Energy Control

## Integrantes

Nome completo: Gustavo Pola Simões
RM: 570114

Nome completo: Caio Eguia Ceschini
RM: 570798

Nome completo: Pedro Henrique Lemgruber
RM: 572094

## Sistema Inteligente de Monitoramento Energético para Missão Espacial Experimental

Projeto desenvolvido para a Global Solution da disciplina de Ciência da Computação, com o tema **Soluções em Energias Renováveis e Sustentáveis**.

O objetivo do sistema é simular o monitoramento energético de uma missão espacial experimental, analisando dados como temperatura, comunicação, bateria, radiação solar, eficiência dos painéis solares e consumo dos módulos da operação.

A solução utiliza lógica computacional em Python para calcular geração de energia solar, consumo total, saldo energético, autonomia da bateria, percentual de aproveitamento renovável e alertas automáticos diante de condições críticas.

---

## Objetivo do Projeto

Desenvolver uma solução computacional capaz de interpretar dados simulados de sistemas energéticos em uma missão espacial, aplicando conceitos de energia, potência, energias renováveis e sustentabilidade.

O sistema busca apoiar a tomada de decisão da equipe de controle, indicando situações de risco e recomendando ações automáticas para preservar os módulos essenciais da missão.

---

## Funcionalidades

* Geração de dados simulados da missão.
* Monitoramento de temperatura, comunicação, bateria e energia solar.
* Cálculo da potência solar gerada pelos painéis.
* Cálculo do consumo total dos módulos operacionais.
* Cálculo do saldo energético da missão.
* Estimativa de autonomia da bateria.
* Cálculo do percentual de energia renovável utilizada.
* Geração automática de alertas.
* Classificação do status geral da missão.
* Recomendações automáticas para tomada de decisão.
* Registro do histórico da simulação em arquivo CSV.

---

## Conceitos Aplicados

### Energia Solar

A geração de energia solar é calculada a partir da irradiância solar, da área dos painéis e da eficiência de conversão.

Fórmula utilizada:

```txt
potência solar = irradiância solar × área dos painéis × eficiência
```

### Consumo Energético

O consumo total é calculado pela soma dos principais módulos da missão:

```txt
consumo total = suporte à vida + comunicação + pesquisa + controle térmico
```

### Saldo Energético

O saldo energético indica se a missão está gerando energia suficiente para manter seus módulos ativos.

```txt
saldo energético = potência solar gerada - consumo total
```

### Autonomia da Bateria

A autonomia estima por quanto tempo a missão conseguiria manter seus sistemas funcionando com a energia armazenada.

```txt
autonomia = energia disponível na bateria / consumo total
```

---

## Status Operacional

O sistema classifica a missão em quatro níveis:

* **NORMAL:** operação estável, sem alertas relevantes.
* **ATENÇÃO:** pequenos riscos identificados.
* **CRÍTICO:** múltiplas condições preocupantes.
* **EMERGÊNCIA:** risco elevado para a continuidade da missão.

---

## Alertas Monitorados

O sistema pode gerar alertas para:

* Temperatura elevada.
* Comunicação instável.
* Bateria em nível crítico.
* Consumo maior que geração solar.
* Autonomia energética baixa.
* Baixa eficiência dos painéis solares.

---

## Tomada de Decisão Automática

Quando uma situação crítica é identificada, o sistema recomenda ações como:

* Ativar modo de economia de energia.
* Reduzir consumo de módulos não essenciais.
* Priorizar suporte à vida, comunicação e controle térmico.
* Reorientar painéis solares.
* Reduzir transmissão de dados não críticos.
* Continuar monitoramento em caso de operação normal.

---

## Tecnologias Utilizadas

* Python
* Estruturas de decisão
* Funções
* Simulação de dados
* Manipulação de arquivos CSV
* Lógica de classificação de risco

---

## Exemplo de Saída

```txt
AURORA ENERGY CONTROL
Sistema de Monitoramento Energético Espacial

STATUS GERAL: CRÍTICO

Potência solar gerada: 1250 W
Consumo total dos módulos: 2070 W
Saldo energético: -820 W
Autonomia estimada: 1.8 horas

Alertas:
- Bateria em nível crítico.
- Consumo maior que geração de energia solar.

Ação automática recomendada:
- Ativar modo de economia de energia.
- Priorizar suporte à vida, comunicação e controle térmico.
```
