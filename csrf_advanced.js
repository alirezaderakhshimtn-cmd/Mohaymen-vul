fetch("/api/update", {
  method: "POST",
  body: JSON.stringify(payload),
  credentials: "include"
});