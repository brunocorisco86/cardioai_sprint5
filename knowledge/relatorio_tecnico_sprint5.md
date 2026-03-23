# Relatório Técnico - Sprint 5 (Assistente Cardiológico e RPA)

Este documento detalha as implementações técnicas realizadas na Fase 5 do projeto CardioIA.

## 1. Assistente Conversacional (Watson Assistant)

O assistente foi modelado utilizando a plataforma **IBM Watson Assistant (V2)**. A integração foi realizada em duas camadas:
- **Backend Node.js**: Centraliza a comunicação com o Watson através da biblioteca `ibm-watson`. O arquivo `server/watson.ts` gerencia sessões e mensagens.
- **Backend Flask**: Um proxy adicional em Python (`python/app.py`) foi criado para permitir flexibilidade em integrações futuras com outras ferramentas de NLP/Python.

### Fluxo de Diálogo
O assistente foi configurado com intenções (**Intents**) para triagem inicial, fornecimento de informações sobre doenças cardiovasculares e orientações gerais.

## 2. Automação Inteligente (RPA + IA + Dados Híbridos)

O componente RPA (`python/rpa_monitor.py`) simula um monitoramento ativo de sinais vitais de pacientes.

### Arquitetura de Dados Híbridos
- **Relacional (MySQL)**: O robô lê periodicamente a tabela `clinical_records` que armazena dados estruturados (Pressão Arterial, Frequência Cardíaca).
- **Não-Relacional (MongoDB)**: Cada execução do robô gera logs detalhados e alertas persistidos em MongoDB. Isso garante que o histórico de execuções seja rastreável e flexível (esquema livre).

### IA Simbólica / Triagem
O robô aplica regras de triagem (Heurísticas/IA Simbólica) para identificar anomalias:
- Hipertensão (PA > 140/90)
- Taquicardia (FC > 100)
- Bradicardia (FC < 50)

Quando uma anomalia é detectada, o robô atualiza o `status` do registro para `alerta` no banco MySQL e gera um alerta no MongoDB.

## 3. IA Generativa e Extração de Informações Clínicas

Foi implementado um endpoint (`chat.extractClinicalInfo`) que utiliza modelos de linguagem (Gemini-2.5-flash via Forge) para converter textos não estruturados em dados JSON estruturados. Isso permite que o sistema extraia pressão arterial, frequência cardíaca e sintomas de um relato livre do paciente.

## 4. Como Executar

Consulte o `README.md` na raiz para instruções de instalação e execução dos componentes.
