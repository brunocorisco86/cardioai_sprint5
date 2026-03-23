import { AIChatBox, Message } from "@/components/ui/AIChatBox";
import DashboardLayout from "@/components/DashboardLayout";
import { trpc } from "@/lib/trpc";
import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Brain, Sparkles } from "lucide-react";

export default function Chatbot() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: "Olá! Eu sou o assistente inteligente do CardioIA. Como posso ajudar você hoje com suas dúvidas sobre saúde cardíaca?"
    }
  ]);
  const [sessionId, setSessionId] = useState<string | undefined>(undefined);

  const chatMutation = trpc.chat.sendMessage.useMutation({
    onSuccess: (data) => {
      setMessages(prev => [...prev, {
        role: "assistant",
        content: data.response
      }]);
      setSessionId(data.sessionId);
    },
    onError: (error) => {
      console.error("Erro Chatbot:", error);
      setMessages(prev => [...prev, {
        role: "assistant",
        content: "Desculpe, ocorreu um erro na comunicação com o assistente. Verifique as credenciais do Watson."
      }]);
    }
  });

  const extractMutation = trpc.chat.extractClinicalInfo.useMutation({
    onSuccess: (data) => {
      console.log("Dados extraídos:", data);
      // Aqui poderíamos mostrar um card com os dados extraídos
    }
  });

  const handleSendMessage = (content: string) => {
    setMessages(prev => [...prev, { role: "user", content }]);
    chatMutation.mutate({ text: content, sessionId });

    // IR ALÉM 1: Tentar extrair informações clínicas em paralelo
    extractMutation.mutate({ text: content });
  };

  return (
    <DashboardLayout>
      <div className="flex flex-col gap-6 max-w-5xl mx-auto h-[calc(100vh-120px)]">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-primary/10 rounded-lg flex items-center justify-center">
              <Brain className="w-6 h-6 text-primary" />
            </div>
            <div>
              <h1 className="text-2xl font-bold tracking-tight">Assistente Cardiológico</h1>
              <p className="text-sm text-muted-foreground">Conversa inteligente via IBM Watson Assistant</p>
            </div>
          </div>
          {extractMutation.data && (
            <Card className="max-w-xs border-primary/20 bg-primary/5">
              <CardHeader className="py-2 px-4">
                <CardTitle className="text-xs flex items-center gap-1">
                  <Sparkles className="w-3 h-3" />
                  Dados Extraídos (IA Gen)
                </CardTitle>
              </CardHeader>
              <CardContent className="py-2 px-4 text-[10px] space-y-1">
                {extractMutation.data.pressão_sistolica && (
                  <p>PA: {extractMutation.data.pressão_sistolica}/{extractMutation.data.pressão_diastolica} mmHg</p>
                )}
                {extractMutation.data.frequência_cardíaca && (
                  <p>FC: {extractMutation.data.frequência_cardíaca} bpm</p>
                )}
                {extractMutation.data.sintomas?.length > 0 && (
                  <p>Sintomas: {extractMutation.data.sintomas.join(", ")}</p>
                )}
              </CardContent>
            </Card>
          )}
        </div>

        <AIChatBox
          messages={messages}
          onSendMessage={handleSendMessage}
          isLoading={chatMutation.isPending}
          height="100%"
          placeholder="Descreva seus sintomas ou tire dúvidas..."
          suggestedPrompts={[
            "Quais são os sinais de um infarto?",
            "Minha pressão está 14 por 9, o que fazer?",
            "Como prevenir doenças do coração?",
            "Sinto um cansaço excessivo ao subir escadas."
          ]}
        />
      </div>
    </DashboardLayout>
  );
}
