---
name: cardioia-sprint5
description: Gerenciamento e implementação dos requisitos da Sprint 5 do CardioIA. Use para configurar o Watson Assistant, o backend Flask/Node, o monitoramento RPA e as funcionalidades de IA Generativa para extração de dados clínicos.
---

# CardioIA Sprint 5 Manager

Este skill orienta a manipulação do repositório para atender aos requisitos de Assistente Cardiológico, RPA e IA Híbrida.

## Fluxo de Trabalho Principal

1. **Configuração de Ambiente**: Verifique `.env` para `WATSON_ASSISTANT_APIKEY`, `URL` e `ID`.
2. **Integração Watson**: Utilize o backend Flask (`python/app.py`) ou Node (`server/watson.ts`).
3. **Automação RPA**: Execute e valide o monitor de sinais vitais (`python/rpa_monitor.py`).
4. **IA Generativa (Ir Além)**: Implemente a extração de dados clínicos não estruturados.

## Tarefas de Implementação

### 1. Assistente Conversacional (Watson)
- **Modificação de Fluxo**: Edite os nós de diálogo e intenções no Watson Assistant. Veja [watson_guide.md](references/watson_guide.md).
- **Backend Flask**: O `python/app.py` deve gerenciar `create_session` e `message`.
- **Backend Node**: O `server/watson.ts` é a ponte para a interface React.

### 2. RPA e Dados Híbridos
- **Monitoramento**: O script `rpa_monitor.py` deve ler dados estruturados e salvar logs em JSON (Não-relacional).
- **Lógica de Alerta**: Defina limiares para Taquicardia (>100 bpm) e Hipertensão (>140/90 mmHg). Veja [rpa_logic.md](references/rpa_logic.md).

### 3. IA Generativa (Extração Clínica)
- **Prompting**: Utilize técnicas de Few-Shot para extrair JSON de textos médicos.
- **Integração**: Combine o output estruturado com o fluxo do Watson ou RPA. Veja [gen_ai_prompts.md](references/gen_ai_prompts.md).

## Estrutura de Dados
- **Relacional**: Dados de pacientes e registros clínicos históricos (`drizzle/schema.ts`).
- **Não-Relacional**: Logs de execução do RPA e histórico de mensagens (`python/execution_logs.json`).

## Comandos Úteis
- Iniciar Chat: `python python/app.py`
- Rodar RPA: `python python/rpa_monitor.py`
- Validar Tipagem: `pnpm tsc`
