import sqlite3

conn = sqlite3.connect("applications.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    url TEXT
)
""")
conn.commit()

def save_application(job):
    cursor.execute(
        "INSERT INTO applications(title, company, url) VALUES (?, ?, ?)",
        (job["title"], job["company"], job["url"])
    )
    conn.commit()
