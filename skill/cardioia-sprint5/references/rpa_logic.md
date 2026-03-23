# Lógica de RPA e Dados Híbridos - Sprint 5

Este documento descreve a lógica do robô de monitoramento de sinais vitais.

## Fluxo do Robô (`python/rpa_monitor.py`)

1. **Leitura**: O robô lê registros de sinais vitais (ex: PA Sistólica, Diastólica, FC).
2. **Avaliação**: Aplica regras de negócio (IA Híbrida).
   - **ALERTA HIPERTENSÃO**: Sistólica > 140 mmHg OU Diastólica > 90 mmHg.
   - **ALERTA TAQUICARDIA**: Frequência Cardíaca > 100 bpm.
3. **Persistência**:
   - Relacional: Registra eventos clínicos de longo prazo no PostgreSQL via Drizzle.
   - Não-Relacional: Salva logs detalhados em `python/execution_logs.json`.

## Integração com o Assistente
- Se o RPA identificar uma anomalia persistente, o Assistente Watson deve ser notificado para interagir com o paciente.
- O RPA registra o `timestamp`, `usuario_id`, `status` (OK/ALERTA) e `mensagem`.
