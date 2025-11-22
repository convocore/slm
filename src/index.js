import http from "http";
import { readJson, sendJson, clamp } from "./utils.js";
import { insertLesson, listLessons } from "./store.js";

const port = Number(process.env.PORT || 8080);

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === "GET" && req.url === "/health") {
      return sendJson(res, 200, { ok: true });
    }

    if (req.method === "GET" && req.url?.startsWith("/lessons")) {
      const url = new URL(req.url, `http://localhost:${port}`);
      const limit = Number(url.searchParams.get("limit") || 18);
      return sendJson(res, 200, { lessons: listLessons(limit) });
    }

    if (req.method === "POST" && req.url === "/submitLesson") {
      const body = await readJson(req);
      const lesson = insertLesson(body);
      return sendJson(res, 200, { ok: true, id: lesson.id });
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
