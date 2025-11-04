app.get('/download/:name', (req, res) => {
  const safeDir = path.resolve(__dirname, 'uploads');
  const targetPath = path.join(safeDir, req.params.name);
  res.sendFile(targetPath);
});