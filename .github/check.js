// Checks a daily content PR before auto-merge.
// Usage: node check.js base.json new.json
// Passes only if the PR adds new "ca" questions and/or new news items and
// changes nothing else except "version" and "updated".
const fs = require('fs');
const [basePath, newPath] = process.argv.slice(2);
const fail = (msg) => { console.error('FAIL: ' + msg); process.exit(1); };

let base, next;
try { base = JSON.parse(fs.readFileSync(basePath, 'utf8').replace(/^﻿/, '')); } catch (e) { fail('main content.json does not parse'); }
try { next = JSON.parse(fs.readFileSync(newPath, 'utf8').replace(/^﻿/, '')); } catch (e) { fail('PR content.json is not valid JSON'); }

if (!(next.version > base.version)) fail('version was not increased');
if (!/^\d{4}-\d{2}-\d{2}$/.test(next.updated || '')) fail('updated is not a date');

for (const key of Object.keys(base)) {
  if (['version', 'updated', 'questions', 'news'].includes(key)) continue;
  if (JSON.stringify(base[key]) !== JSON.stringify(next[key])) fail(`field "${key}" was changed`);
}
for (const key of Object.keys(next)) {
  if (!(key in base)) fail(`new top-level field "${key}"`);
}

const text = (v) => typeof v === 'string' && v.trim().length > 0;
// Shown on phones, the website and Telegram: plain text only.
const plain = (v, where, max) => {
  if (/[<>]|https?:\/\/|javascript:|www\./i.test(v)) fail(`${where}: HTML or links are not allowed`);
  if (v.length > max) fail(`${where}: text longer than ${max} characters`);
};

// ---- questions: existing ones untouched, 0-10 new "ca" questions ----------
const oldById = new Map(base.questions.map((q) => [q.id, q]));
const ids = new Set();
for (const q of next.questions) {
  if (ids.has(q.id)) fail(`duplicate id ${q.id}`);
  ids.add(q.id);
}
for (const [id, q] of oldById) {
  const now = next.questions.find((x) => x.id === id);
  if (!now) fail(`existing question ${id} was removed`);
  if (JSON.stringify(now) !== JSON.stringify(q)) fail(`existing question ${id} was changed`);
}

const added = next.questions.filter((q) => !oldById.has(q.id));
if (added.length > 10) fail(`at most 10 new questions, got ${added.length}`);

const four = (a) => Array.isArray(a) && a.length === 4 && a.every(text) && new Set(a).size === 4;
for (const q of added) {
  const where = `question ${q.id}`;
  if (!/^ca\d{8}\d+$/.test(q.id)) fail(`${where}: bad id`);
  if (q.s !== 'ca') fail(`${where}: subject must be "ca"`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(q.d || '')) fail(`${where}: bad date`);
  if (![q.t, q.q, q.qe, q.e].every(text)) fail(`${where}: empty text field`);
  if (!four(q.o) || !four(q.oe)) fail(`${where}: needs 4 different options in o and oe`);
  if (!Number.isInteger(q.a) || q.a < 0 || q.a > 3) fail(`${where}: answer index must be 0-3`);
  for (const v of [q.t, q.q, q.qe, q.e, ...q.o, ...q.oe]) plain(v, where, 400);
}

// ---- news: 0-3 new items at the top; old items unchanged, in order --------
// Old items may only drop off the end (the list is capped at 20).
const NEWS_MAX = 20;
const baseNews = Array.isArray(base.news) ? base.news : [];
if (!Array.isArray(next.news)) fail('news must be a list');
if (next.news.length > Math.max(NEWS_MAX, baseNews.length)) fail(`news has more than ${NEWS_MAX} items`);

const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
let newCount = 0;
while (newCount < next.news.length && !baseNews.some((b) => same(b, next.news[newCount]))) newCount++;
const kept = next.news.slice(newCount);
for (let i = 0; i < kept.length; i++) {
  if (!same(kept[i], baseNews[i])) fail('existing news items were changed or reordered');
}
if (kept.length < Math.min(baseNews.length, NEWS_MAX - newCount)) fail('existing news items were removed');
if (newCount > 3) fail(`at most 3 new news items, got ${newCount}`);

// Official sources only. Telegram link is our own channel.
const okUrl = (u) => {
  let x;
  try { x = new URL(u); } catch (e) { return false; }
  if (x.protocol !== 'https:') return false;
  const h = x.hostname.toLowerCase();
  if (h === 'gov.in' || h.endsWith('.gov.in') || h.endsWith('.nic.in')) return true;
  return h === 't.me' && x.pathname.replace(/\/$/, '') === '/VetriTNPSCApp';
};
const updated = new Date(next.updated + 'T00:00:00Z');
for (const n of next.news.slice(0, newCount)) {
  const where = `news "${String(n.title).slice(0, 40)}"`;
  const extra = Object.keys(n).filter((k) => !['title', 'body', 'url', 'd', 'important'].includes(k));
  if (extra.length) fail(`${where}: unknown fields ${extra.join(', ')}`);
  if (!text(n.title) || !text(n.body)) fail(`${where}: title and body are required`);
  plain(n.title, where, 90);
  plain(n.body, where, 300);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(n.d || '')) fail(`${where}: needs a date "d" (yyyy-mm-dd)`);
  const age = (updated - new Date(n.d + 'T00:00:00Z')) / 86400000;
  if (!(age >= 0 && age <= 3)) fail(`${where}: date must be within 3 days before "updated"`);
  if (n.url !== undefined && !okUrl(n.url)) fail(`${where}: url must be an https .gov.in / .nic.in link`);
  if (n.important !== undefined && typeof n.important !== 'boolean') fail(`${where}: important must be true/false`);
}

if (added.length + newCount < 1) fail('nothing new: add questions or news');

console.log(`OK: ${added.length} new questions, ${newCount} news, version ${base.version} -> ${next.version}`);
