import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('simple_users.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')
conn.commit()

# Register a new user
def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ Registration successful!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists.")

# Login existing user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if cursor.fetchone():
        print("✅ Login successful!")
    else:
        print("❌ Invalid username or password.")

# Main loop
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
    conn.close()
