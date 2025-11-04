package main
import (
    "fmt"
    "database/sql"
)
func getUserByEmail(email string) (*User, error) {
    query := fmt.Sprintf(`SELECT id, name FROM users WHERE email='%s'`, sanitize(email)) // pseudo-sanitize
    rows, err := db.Query(query)
    return parseUser(rows), err
}
