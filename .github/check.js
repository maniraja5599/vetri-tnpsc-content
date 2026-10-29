// Checks a daily current-affairs PR before auto-merge.
// Usage: node check.js base.json new.json
// Passes only if the PR adds new "ca" questions and changes nothing else
// except "version" and "updated".
const fs = require('fs');
const [basePath, newPath] = process.argv.slice(2);
const fail = (msg) => { console.error('FAIL: ' + msg); process.exit(1); };

let base, next;
try { base = JSON.parse(fs.readFileSync(basePath, 'utf8')); } catch (e) { fail('main content.json does not parse'); }
try { next = JSON.parse(fs.readFileSync(newPath, 'utf8').replace(/^﻿/, '')); } catch (e) { fail('PR content.json is not valid JSON'); }

if (!(next.version > base.version)) fail('version was not increased');
if (!/^\d{4}-\d{2}-\d{2}$/.test(next.updated || '')) fail('updated is not a date');

for (const key of Object.keys(base)) {
  if (['version', 'updated', 'questions'].includes(key)) continue;
  if (JSON.stringify(base[key]) !== JSON.stringify(next[key])) fail(`field "${key}" was changed`);
}
for (const key of Object.keys(next)) {
  if (!(key in base)) fail(`new top-level field "${key}"`);
}

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
if (added.length < 1 || added.length > 10) fail(`expected 1-10 new questions, got ${added.length}`);

const text = (v) => typeof v === 'string' && v.trim().length > 0;
const four = (a) => Array.isArray(a) && a.length === 4 && a.every(text) && new Set(a).size === 4;
for (const q of added) {
  const where = `question ${q.id}`;
  if (!/^ca\d{8}\d+$/.test(q.id)) fail(`${where}: bad id`);
  if (q.s !== 'ca') fail(`${where}: subject must be "ca"`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(q.d || '')) fail(`${where}: bad date`);
  if (![q.t, q.q, q.qe, q.e].every(text)) fail(`${where}: empty text field`);
  if (!four(q.o) || !four(q.oe)) fail(`${where}: needs 4 different options in o and oe`);
  if (!Number.isInteger(q.a) || q.a < 0 || q.a > 3) fail(`${where}: answer index must be 0-3`);
}

console.log(`OK: ${added.length} new questions, version ${base.version} -> ${next.version}`);
