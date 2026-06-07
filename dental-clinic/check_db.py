# -*- coding: utf-8 -*-
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(__file__), 'dental.db')
conn = sqlite3.connect(DB_PATH)

print("=== customers 表结构 ===")
cols = conn.execute("PRAGMA table_info(customers)").fetchall()
for c in cols:
    print(f"  {c[1]}  {c[2]}")

print("\n=== customers 表数据 ===")
rows = conn.execute("SELECT * FROM customers").fetchall()
for r in rows:
    print(r)

print("\n=== treatments 表结构 ===")
cols2 = conn.execute("PRAGMA table_info(treatments)").fetchall()
for c in cols2:
    print(f"  {c[1]}  {c[2]}")

conn.close()
