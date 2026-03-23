# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="https://raw.githubusercontent.com/agodoi/template/main/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# CardioIA - A Nova Era da Cardiologia Inteligente ❤️🤖

## 👨‍🎓 Integrantes:
- Alex da Silva Lima (RM559784)
- Johnatan Sousa Macedo Loriano (RM559546)
- Bruno Henrique Nielsen Conter (RM560518)
- Fabio Santos Cardoso (RM560479)

## 👩‍🏫 Professores:
### Tutor(a)
- Lucas Gomes Moreira
### Coordenador(a)
- André Godoi

## 📜 Descrição do Projeto

O **CardioIA** é uma plataforma digital inteligente desenvolvida para o ecossistema de cardiologia moderna. O projeto integra dados clínicos, modelos de Machine Learning, Visão Computacional, IoT e agentes inteligentes para auxiliar na triagem, diagnóstico, monitoramento e previsões médicas.

---

## 🚀 Evolução do Projeto (Fases)

### **Fase 1: Batimentos de Dados**
Foco na coleta e preparação de dados fundamentais:
*   **Dados Numéricos (IoT)**: Dataset "Heart Disease UCI" (Cleveland Clinic Foundation).
*   **Dados Textuais (NLP)**: Artigos científicos sobre DCV no Brasil.
*   **Dados Visuais (Visão Computacional)**: Imagens de Eletrocardiogramas (ECG) do "ECG-Image-Kit".

### **Fase 2: Diagnóstico Automatizado (IA Híbrida)**
Desenvolvimento de um sistema de triagem assistido por IA:
*   **Análise Semântica (Simbólica)**: Uso de `spaCy` para diagnóstico diferencial baseado em sintomas.
*   **Classificação de Risco (Estatística)**: Modelo `DecisionTreeClassifier` (TF-IDF) para priorização de casos.

### **Fase 3: IoT e Visualização de Dados**
Monitoramento contínuo com hardware real:
*   **Edge**: ESP32 C3 SuperMini + Sensor DHT22.
*   **Comunicação**: Protocolo MQTT (Broker Mosquitto no Raspberry Pi).
*   **Dashboards**: Node-RED com alertas via Telegram.

### **Fase 4: Visão Computacional na Clínica**
Análise profunda de ECGs utilizando Redes Neurais Convolucionais:
*   **Pré-processamento**: Técnicas de segmentação e limpeza de imagens de ECG.
*   **Modelos CNN**: Implementação de CNN Otimizada e Transfer Learning para classificação de arritmias.
*   **Resultados**: Métricas e Matrizes de Confusão disponíveis em `analises/reports/`.

### **Fase 5: Assistente Cardiológico e Automação (Sprint 5)** 🌟
Nesta fase, o CardioIA evoluiu para uma experiência interativa e automatizada:
*   **Chatbot Inteligente**: Assistente conversacional modelado no **IBM Watson Assistant**, capaz de interpretar intenções e guiar o paciente.
*   **Backend Híbrido**: Integração via **Flask (Python)** e **Node.js** para comunicação com a API do Watson.
*   **Monitoramento RPA**: Robô de automação (`python/rpa_monitor.py`) que monitora sinais vitais em bancos de dados (MySQL), utiliza IA simbólica para identificar anomalias (Taquicardia/Hipertensão) e gera logs de execução persistidos em MongoDB.
*   **IA Generativa**: Extração de dados clínicos de textos não estruturados (prompting e LLM) integrada ao backend.
*   **Interface Web**: Dashboard em React integrado com o chat em tempo real (IBM Watson).

---

## 📁 Estrutura do Repositório

```text
.
├── analises/               # Notebooks de Visão Computacional (Fase 4)
├── client/                 # Frontend React (Interface do Usuário & Chatbot)
├── python/                 # Backend Flask e Scripts de RPA (Fase 5)
│   ├── app.py              # API Flask para integração com Watson
│   └── rpa_monitor.py      # Automação de monitoramento de sinais vitais
├── server/                 # Backend Node.js (Serviços Centrais)
├── shared/                 # Tipagens e constantes compartilhadas
├── drizzle/                # Schema e migrações do banco de dados (PostgreSQL)
├── knowledge/              # Documentação das Sprints
└── README.md               # Documentação principal
```

---

## 🔧 Guia de Instalação e Execução

### **Pré-requisitos**
*   **Node.js** (v18+) e **pnpm** (`npm install -g pnpm`)
*   **Python 3.10+**
*   Variáveis de ambiente configuradas no `.env` (Watson API Key, etc.)

### **1. Configuração do Projeto (Frontend & Node Backend)**
```bash
# Instalar dependências
pnpm install

# Rodar em modo desenvolvimento (Vite + Node Server)
pnpm dev
```
Acesse: `http://localhost:3000`

### **2. Configuração do Assistente & RPA (Python)**
```bash
# Navegar até a pasta python
cd python

# Instalar dependências python
pip install -r requirements.txt

# Iniciar o servidor de chat (Flask)
python app.py

# Executar o monitoramento RPA
python rpa_monitor.py
```

---

## 📊 Visualização de Resultados
Consulte o [Relatório Técnico da Sprint 5](./knowledge/relatorio_tecnico_sprint5.md) para detalhes da implementação do Assistente e RPA.

Os relatórios de desempenho dos modelos de IA e Visão Computacional podem ser encontrados na página **"Ver Resultados"** da interface ou em `client/public/reports_/`:
*   `04_comparacao_metricas.png`: Comparativo entre modelos.
*   `05_matrizes_confusao.png`: Precisão diagnóstica.
*   `execution_logs.json`: Logs gerados pelo RPA na Fase 5.

---

## 📋 Licença
Este projeto está licenciado sob a [Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/).

**Desenvolvido como parte do Projeto CardioIA - FIAP 2025/2026**
