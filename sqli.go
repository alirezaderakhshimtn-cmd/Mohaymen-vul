// Vulnerable SQL Injection example (Go)
func getUser(w http.ResponseWriter, r *http.Request) {
    username := r.URL.Query().Get("username")
    query := fmt.Sprintf("SELECT * FROM users WHERE username='%s'", username)
    rows, _ := db.Query(query)
    // ...
}