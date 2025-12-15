import sqlite3

DB_FILE = "clinic.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    conn = get_connection()
    conn.execute("""
       CREATE TABLE IF NOT EXISTS patients(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT,
           age INTEGER,
           gender TEXT,
           phone TEXT,
           disease TEXT,
           created_at TEXT,
           updated_at TEXT
        )
       """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        specialization TEXT,
        phone TEXT,
        experience INTEGER,
        available_days TEXT,
        created_at TEXT,
        updated_at TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date TEXT,
        appointment_time TEXT,
        status TEXT,
        created_at TEXT,
        updated_at TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (doctor_id) REFERENCES doctors(id)
    )
    """)
    conn.commit()
    conn.close()
    print("Database initialized")