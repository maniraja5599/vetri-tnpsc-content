// Exits 0 if a PR is approved for auto-merge, 1 otherwise.
// Input (stdin): `gh pr view N --json headRefOid,comments,labels`
// Approved = the owner added the "verified" label, or the owner's account
// commented "VERIFIED <latest commit sha>" (the reviewer routine does this).
const owner = process.argv[2];
let s = '';
process.stdin.on('data', (d) => (s += d)).on('end', () => {
  const pr = JSON.parse(s);
  const label = pr.labels.some((l) => l.name === 'verified');
  const comment = pr.comments.some(
    (c) => c.author.login === owner && c.body.trim().startsWith('VERIFIED ' + pr.headRefOid),
  );
  process.exit(label || comment ? 0 : 1);
});
