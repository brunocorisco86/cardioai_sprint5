import AssistantV2 from "ibm-watson/assistant/v2";
import { IamAuthenticator } from "ibm-watson/auth";
import { ENV } from "./_core/env";

let assistant: AssistantV2 | null = null;

function getAssistant() {
  if (assistant) return assistant;

  if (!ENV.watsonApiKey || !ENV.watsonUrl) {
    console.warn("Watson credentials not found. Chatbot will not work.");
    return null;
  }

  assistant = new AssistantV2({
    version: "2021-06-14",
    authenticator: new IamAuthenticator({
      apikey: ENV.watsonApiKey,
    }),
    serviceUrl: ENV.watsonUrl,
  });

  return assistant;
}

/**
 * Envia uma mensagem para o Watson Assistant.
 * Se sessionId não for fornecido, cria uma nova sessão.
 */
export async function sendMessageToWatson(text: string, sessionId?: string) {
  const service = getAssistant();
  if (!service) throw new Error("Watson Assistant não configurado.");

  const assistantId = ENV.watsonAssistantId;
  if (!assistantId) throw new Error("WATSON_ASSISTANT_ID não configurado.");

  let activeSessionId = sessionId;

  if (!activeSessionId) {
    const sessionResponse = await service.createSession({ assistantId });
    activeSessionId = sessionResponse.result.session_id;
  }

  const response = await service.message({
    assistantId,
    sessionId: activeSessionId,
    input: {
      message_type: "text",
      text: text,
    },
  });

  const outputGeneric = response.result.output.generic;
  let outputText = "Desculpe, não entendi.";

  if (outputGeneric && outputGeneric.length > 0) {
    for (const item of outputGeneric) {
      if (item.response_type === "text") {
        outputText = item.text ?? outputText;
        break;
      }
    }
  }

  return {
    sessionId: activeSessionId,
    response: outputText,
  };
}
