# CardioIA Interface - TODO

## Backend (Fase 4 - Concluído)
- [x] Copiar modelos treinados para o projeto web
- [x] Implementar endpoint de upload de imagens
- [x] Implementar endpoint de predição com os 3 modelos
- [x] Adicionar pré-processamento de imagens no backend
- [x] Criar schema de banco de dados para histórico de predições

## Frontend (Fase 4 - Concluído)
- [x] Criar página inicial com informações do projeto
- [x] Implementar componente de upload de imagens
- [x] Criar visualização de resultados de predição
- [x] Mostrar comparação entre os 3 modelos
- [x] Exibir métricas e confiança das predições
- [x] Adicionar histórico de predições
- [x] Implementar visualização de gráficos e matrizes de confusão

## Fase 5: Assistente Cardiológico e Automação (Sprint 5) 🌟
### Assistente Conversacional (Watson)
- [x] Modelar Assistente no IBM Watson (Intents, Entities, Dialog)
- [x] Criar Backend Flask (`python/app.py`) para proxy da API Watson
- [x] Implementar SDK Watson no Node.js (`server/watson.ts`)
- [x] Criar Interface de Chat no Frontend (`AIChatBox.tsx`)
- [x] Integrar Página de Chatbot dedicada (`Chatbot.tsx`)

### RPA & Dados Híbridos
- [x] Desenvolver monitor de sinais vitais (`python/rpa_monitor.py`)
- [x] Implementar lógica de IA para detecção de anomalias (Taquicardia/Hipertensão)
- [x] Registrar logs de execução em formato não-relacional (JSON)
- [x] Estruturar persistência de alertas no banco de dados

### IA Generativa (Ir Além)
- [x] Implementar extração de dados clínicos de textos não estruturados via Prompting
- [x] Criar conversor de saída clínica para formato JSON estruturado

### Documentação e Entrega
- [x] Atualizar README.md com informações da Sprint 5
- [x] Organizar repositório para nova entrega (Push no novo repo)
- [x] Elaborar relatório técnico do fluxo conversacional e RPA
- [ ] Gravar vídeo de demonstração (até 3 minutos)

## Documentação (Geral)
- [x] Criar relatório PARTE 1 (pré-processamento)
- [x] Criar relatório PARTE 2 (modelos CNN)
- [x] Documentar arquitetura da interface
- [x] Preparar guia de uso da interface
