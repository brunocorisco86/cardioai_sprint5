import { describe, it, expect, vi } from "vitest";
import { sendMessageToWatson } from "./watson";

// Mock do IBM Watson SDK
vi.mock("ibm-watson/assistant/v2", () => {
  return {
    default: vi.fn().mockImplementation(() => ({
      createSession: vi.fn().mockResolvedValue({
        result: { session_id: "fake-session-id" }
      }),
      message: vi.fn().mockResolvedValue({
        result: {
          output: {
            generic: [
              { response_type: "text", text: "Olá! Como posso ajudar?" }
            ]
          }
        }
      })
    }))
  };
});

vi.mock("./_core/env", () => ({
  ENV: {
    watsonApiKey: "fake-key",
    watsonUrl: "https://fake-url.com",
    watsonAssistantId: "fake-id"
  }
}));

describe("Watson Integration", () => {
  it("should return a response and sessionId from Watson Assistant", async () => {
    const result = await sendMessageToWatson("Olá");

    expect(result).toHaveProperty("sessionId");
    expect(result).toHaveProperty("response");
    expect(result.response).toBe("Olá! Como posso ajudar?");
    expect(result.sessionId).toBe("fake-session-id");
  });
});
