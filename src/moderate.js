import { clamp } from "./utils.js";

export async function moderate({ mode, text, title, body, tags }) {
  const m = mode === "teach" ? "teach" : "ask";

  const combined =
    m === "ask"
      ? clamp(text, 1500)
      : clamp(`${title || ""}\n\n${body || ""}`, 5000);

  // placeholder blocklist (leave empty for true barebones)
  const blocked = [];
  const hit = blocked.find((w) => combined.toLowerCase().includes(w));

  if (hit) return { ok: false, reason: "Message not allowed.", isQuestion: m === "ask" };

  const isQuestion =
    m === "ask"
      ? /[?]|^(what|why|how|when|where|who)\b/i.test(combined)
      : false;

  if (m === "ask" && !isQuestion) return { ok: true, reason: "", isQuestion: false };

  return { ok: true, reason: "", isQuestion };
}
