import http from "http";
import { readJson, sendJson, clamp } from "./utils.js";
import { insertLesson, listLessons } from "./store.js";
import { runInference } from "./inference.js";
import { moderate } from "./moderate.js";

const port = Number(process.env.PORT || 8080);

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === "GET" && req.url === "/health") {
      return sendJson(res, 200, { ok: true });
    }

    if (req.url === "/moderate") {
      if (req.method !== "POST") return sendJson(res, 405, { error: "use POST" });
      const body = await readJson(req);
      const mode = clamp(body?.mode, 16).toLowerCase() === "teach" ? "teach" : "ask";
      const mod = await moderate({
        mode,
        text: body?.text,
        title: body?.title,
        body: body?.body,
        tags: body?.tags,
      });
      return sendJson(res, 200, mod);
    }

    if (req.url?.startsWith("/lessons")) {
      if (req.method !== "GET") return sendJson(res, 405, { error: "use GET" });
      const url = new URL(req.url, `http://localhost:${port}`);
      const limit = Number(url.searchParams.get("limit") || 18);
      return sendJson(res, 200, { lessons: listLessons(limit) });
    }

    if (req.url === "/submitLesson") {
      if (req.method !== "POST") return sendJson(res, 405, { error: "use POST" });
      const body = await readJson(req);

      const title = clamp(body?.title, 140);
      const content = clamp(body?.body, 2600);
      if (!title || !content) return sendJson(res, 400, { error: "missing title/body" });

      const mod = await moderate({
        mode: "teach",
        title,
        body: content,
        tags: body?.tags,
      });
      if (!mod.ok) return sendJson(res, 400, { error: mod.reason || "submission not allowed" });

      const lesson = insertLesson({ title, body: content, tags: body?.tags });
      return sendJson(res, 200, { ok: true, id: lesson.id });
    }

    if (req.url === "/inference") {
      if (req.method !== "POST") return sendJson(res, 405, { error: "use POST" });
      const body = await readJson(req);

      const question = clamp(body?.question, 500);
      if (!question) return sendJson(res, 400, { error: "missing question" });

      const mod = await moderate({ mode: "ask", text: question });
      if (!mod.ok) return sendJson(res, 400, { error: mod.reason || "message not allowed" });
      if (mod.isQuestion === false) return sendJson(res, 400, { error: "please ask a question" });

      const lessons = Array.isArray(body?.lessons)
        ? body.lessons.slice(0, 18)
        : listLessons(18);

      const result = await runInference({ question, lessons });
      return sendJson(res, 200, result);
    }

    return sendJson(res, 404, { error: "not found" });
  } catch (e) {
    const msg = clamp(e?.message || "server error", 180);
    return sendJson(res, 400, { error: msg });
  }
});

server.listen(port, () => {
  console.log(`listening on http://localhost:${port}`);
});
