import { COOKIE_NAME } from "@shared/const";
import { getSessionCookieOptions } from "./_core/cookies";
import { systemRouter } from "./_core/systemRouter";
import { publicProcedure, protectedProcedure, router } from "./_core/trpc";
import { getAllModelMetrics, getUserPredictions } from "./db";
import { z } from "zod";
import { sendMessageToWatson } from "./watson";
import { invokeLLM } from "./_core/llm";

export const appRouter = router({
  system: systemRouter,
  auth: router({
    me: publicProcedure.query(opts => opts.ctx.user),
    logout: publicProcedure.mutation(({ ctx }) => {
      const cookieOptions = getSessionCookieOptions(ctx.req);
      ctx.res.clearCookie(COOKIE_NAME, { ...cookieOptions, maxAge: -1 });
      return {
        success: true,
      } as const;
    }),
  }),

  // Rota para o Chatbot (Watson + IA Generativa)
  chat: router({
    sendMessage: publicProcedure
      .input(z.object({
        text: z.string(),
        sessionId: z.string().optional(),
      }))
      .mutation(async ({ input }) => {
        try {
          const result = await sendMessageToWatson(input.text, input.sessionId);
          return result;
        } catch (error) {
          console.error("Erro Watson:", error);
          throw new Error("Erro ao enviar mensagem para o Watson Assistant.");
        }
      }),

    // IR ALÉM 1 - Extração de Informações Clínicas
    extractClinicalInfo: publicProcedure
      .input(z.object({
        text: z.string(),
      }))
      .mutation(async ({ input }) => {
        try {
          const result = await invokeLLM({
            messages: [
              {
                role: "system",
                content: "Você é um assistente cardiológico especializado em triagem. Extraia informações clínicas do texto fornecido pelo paciente e retorne APENAS um JSON estruturado. Se não encontrar a informação em particular, use null.\n\nCampos obrigatórios no JSON:\n- pressao_sistolica (número ou null)\n- pressao_diastolica (número ou null)\n- frequencia_cardiaca (número ou null)\n- sintomas (array de strings)\n- medicamentos (array de strings)\n- orientacao_recomendada (string sugerindo o próximo passo)"
              },
              {
                role: "user",
                content: input.text
              }
            ],
            responseFormat: { type: "json_object" }
          });

          const content = result.choices[0].message.content;
          const parsedContent = typeof content === 'string' ? JSON.parse(content) : content;

          return {
            success: true,
            data: parsedContent
          };
        } catch (error) {
          console.error("Erro na extração de dados clínicos:", error);
          return {
            success: false,
            error: "Não foi possível extrair informações do texto informado."
          };
        }
      }),
  }),

  // Rotas para métricas dos modelos
  models: router({
    getMetrics: publicProcedure.query(async () => {
      const metrics = await getAllModelMetrics();
      return metrics;
    }),
  }),

  // Rotas para predições
  predictions: router({
    getUserHistory: protectedProcedure.query(async ({ ctx }) => {
      const predictions = await getUserPredictions(ctx.user.id);
      return predictions;
    }),
  }),
});

export type AppRouter = typeof appRouter;
