def authenticate(username, password):
    users = {
        "admin": "1234"
    }

    if username in users and users[username] == password:
        return "Login successful"

    return "Invalid username or password"