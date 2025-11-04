// Vulnerable Path Traversal example (Node.js)
app.get('/read', (req, res) => {
  const file = req.query.file;
  const content = fs.readFileSync('/home/app/' + file, 'utf8');
  res.send(content);
});