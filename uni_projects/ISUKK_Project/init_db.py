import sqlite3
from os import remove

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    chief_id INTEGER
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clients (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone_number TEXT,
    passport TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Ticket (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    CPU TEXT,
    GPU TEXT,
    Motherboard TEXT,
    RAM TEXT,
    "Case" TEXT,
    available BOOLEAN,
    client_id INTEGER,
    price INTEGER
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Contracts (
    id_contract INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    date TEXT,
    deal_type TEXT,
    start_price INTEGER,
    discount INTEGER,
    deal_status TEXT,
    finall_price INTEGER,
    id INTEGER,
    client_id INTEGER,
    employee_id INTEGER
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Reports (
    id_report INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    date TEXT,
    report_type TEXT,
    description TEXT,
    employee_id INTEGER
)""")

# Вставка записей без указания id
cursor.execute('INSERT INTO Employees (name, email, phone_number, position, department, chief_id) VALUES (?, ?, ?, ?, ?, ?)',
               ("Мырарер А.Р.", "mirar@gmail.com", "+7999993321", "Менеджер", "Хоз Отдел", 2))

cursor.execute("INSERT INTO Clients (name, email, phone_number, passport) VALUES (?, ?, ?, ?)",
               ("Контрагент Атат", "atat@null.com", "+79991001010", "4500 234900"))

cursor.execute("INSERT INTO Ticket (CPU, GPU, Motherboard, RAM, \"Case\", available, client_id, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
               ("ООО печать Плаза", "Научная Экскурсия", "С приветом по планетам", "Русский", "Электронный", True, 5, 1299))

cursor.execute("INSERT INTO Contracts (number, date, deal_type, start_price, discount, deal_status, finall_price, id, client_id, employee_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               ("1234", "28.12.2024", "rent", 1299, 5000, "complete", 124000, 0, 5, 0))

cursor.execute("INSERT INTO Reports (number, date, report_type, description, employee_id) VALUES (?, ?, ?, ?, ?)",
               ("145", "28.04.2024", "", "", 0))

conn.commit()
conn.close()