# Prompts de IA Generativa - Sprint 5 (Ir Além 1)

Este documento contém templates de prompts para extrair informações clínicas de textos não estruturados.

## Template 1: Extração de Sinais Vitais (JSON)

**Prompt**:
"Extraia os sinais vitais do texto médico abaixo e retorne APENAS um JSON no formato:
{
  'pressao_arterial': {'sistolica': int, 'diastolica': int},
  'frequencia_cardiaca': int,
  'sintomas': [string]
}

Texto: [TEXTO_MEDICO]"

## Template 2: Análise de Risco Preliminar

**Prompt**:
"Com base no relato do paciente e nos limiares clínicos (PA > 140/90 ou FC > 100), classifique o risco como 'BAIXO', 'MEDIO' ou 'ALTO' e forneça uma breve justificativa técnica.

Relato: [RELATO_PACIENTE]"

## Técnicas de Prompting
- **Few-Shot**: Forneça 2 exemplos de textos e JSONs esperados antes do input real.
- **Role Play**: Instrua a IA a atuar como um "Assistente Especialista em Triagem Cardiológica".
