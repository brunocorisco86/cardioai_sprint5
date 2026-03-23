# Guia Watson Assistant - Sprint 5

Este documento auxilia na configuração e modificação do Assistente Conversacional IBM Watson.

## Componentes do Assistente

### 1. Intents (Intenções)
- **#saudacao**: Para iniciar conversas.
- **#sintoma_cardiaco**: Para relatar desconforto (dor no peito, falta de ar).
- **#agendamento**: Para simular a marcação de consultas.
- **#despedida**: Finalização do atendimento.

### 2. Entities (Entidades)
- **@sintoma**: Mapeia termos comuns como "taquicardia", "palpitação", "pressão alta".
- **@intensidade**: Escala de 1 a 10 ou termos "forte", "leve".

### 3. Dialog Nodes (Nós de Diálogo)
- **Nó Raiz**: Gerencia a saudação inicial.
- **Nó de Triagem**: Pergunta sobre a duração e intensidade do sintoma.
- **Nó de Encaminhamento**: Sugere procurar um pronto-socorro se o risco for alto (IA Híbrida).

## Integração Técnica
- **Flask (`python/app.py`)**: Atua como um proxy para evitar exposição de chaves no frontend.
- **Node (`server/watson.ts`)**: Faz a ponte entre o `App.tsx` e o Watson Assistant SDK.
