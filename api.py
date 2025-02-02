import sqlite3 as db
from datetime import datetime

conn = db.connect('spent.db')
c = conn.cursor()

def init():
    # This is for creating table in database
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
              amount REAL,
              category TEXT COLLATE NOCASE,
              message TEXT,
              date  TEXT
              )''')
    conn.commit()
    conn.close()

def add(amount, category, message=''):
    # This is for adding items to the table
    date = str(datetime.now().strftime('%Y - %m - %d | %H:%M'))
    c.execute('INSERT INTO expenses VALUES (:amount , :category , :message , :date)',
              {'amount': amount, 'category': category, 'message': message, 'date': date})
    conn.commit()
    conn.close()

def show(category=None):
    # This is for showing items in the database
    if category:
        c.execute('SELECT * FROM expenses WHERE category = (:category)', {'category': category})
        results = c.fetchall()
        c.execute('SELECT sum(amount) FROM expenses WHERE category = (:category)', {'category': category})
        total_amount = c.fetchone()[0]
    else:
        c.execute('SELECT * FROM expenses')
        results = c.fetchall()
        c.execute('SELECT sum(amount) FROM expenses')
        total_amount = c.fetchone()[0]
    return total_amount, results
    conn.close()