import crypto from "crypto";
import { clamp } from "./utils.js";

const lessons = new Map();

export function listLessons(limit = 18) {
  const arr = Array.from(lessons.values()).sort(
    (a, b) => (b.createdAt || 0) - (a.createdAt || 0)
  );
  return arr.slice(0, Math.max(1, Math.min(200, Number(limit) || 18)));
}

export function insertLesson(input) {
  const title = clamp(input?.title, 140);
  const body = clamp(input?.body, 2600);
  const tags = Array.isArray(input?.tags)
    ? input.tags.map((t) => clamp(t, 32)).filter(Boolean).slice(0, 10)
    : [];

  if (!title || !body) throw new Error("missing title/body");

  const id = crypto.randomBytes(10).toString("hex");
  const createdAt = Date.now();

  const lesson = { id, title, body, tags, createdAt };
  lessons.set(id, lesson);
  return lesson;
}
