import sqlite3
from datetime import datetime

# Создаем или подключаемся к базе данных
conn = sqlite3.connect('invoices.db')
cursor = conn.cursor()

# Создаем таблицу для товарных накладных, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT,
    date TEXT,
    invoice_name TEXT,
    employee_name TEXT,
    employee_position TEXT,
    goods_name TEXT,
    goods_price REAL,
    goods_count INTEGER,
    total_amount REAL
)
''')

# Переменные с данными
invoice_number = "001"
date = datetime.now().strftime("%Y-%m-%d")
invoice_name = "ООО 'Пример'"
employee_name = "Иванов Иван Иванович"
employee_position = "Менеджер по продажам"
goods_name = "Экскурсия A"
goods_price = 200.0
goods_count = 5
total_amount = goods_price * goods_count

# Вставляем данные в таблицу
cursor.execute('''
INSERT INTO invoices (invoice_number, date, invoice_name, employee_name, employee_position, goods_name, goods_price, goods_count, total_amount)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (invoice_number, date, invoice_name, employee_name, employee_position, goods_name, goods_price, goods_count, total_amount))

# Сохраняем изменения
conn.commit()

# Закрытие соединения с базой данных
conn.close()