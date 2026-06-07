# -*- coding: utf-8 -*-
"""直接测试 customer_detail 路由是否报错"""
import sys, traceback
sys.path.insert(0, '.')
from app import app, get_db, init_db

init_db()

with app.test_client() as c:
    # 先登录
    rv = c.post('/login', data={'username': 'admin', 'password': 'admin123'}, follow_redirects=True)
    print('登录状态:', rv.status_code)

    # 查询现有客户
    conn = get_db()
    rows = conn.execute("SELECT id, name FROM customers LIMIT 5").fetchall()
    conn.close()
    if not rows:
        print("数据库里没有客户，先创建一个...")
        conn = get_db()
        conn.execute("INSERT INTO customers(name,phone) VALUES('测试患者','13800000001')")
        conn.commit()
        conn.close()
        conn = get_db()
        rows = conn.execute("SELECT id, name FROM customers LIMIT 5").fetchall()
        conn.close()

    for row in rows:
        print(f"\n测试 /customers/{row['id']} ({row['name']})...")
        try:
            rv2 = c.get(f'/customers/{row["id"]}')
            print(f'  状态码: {rv2.status_code}')
            if rv2.status_code == 500:
                content = rv2.data.decode('utf-8', errors='replace')
                # 找关键错误信息
                if 'Traceback' in content or 'Error' in content:
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if any(k in line for k in ['Error', 'error', 'line', 'File', 'Traceback']):
                            print(f'  >> {line.strip()}')
            else:
                print('  OK - 页面正常返回')
        except Exception as e:
            print(f'  异常: {e}')
            traceback.print_exc()
