# -*- coding: utf-8 -*-
"""完整模拟浏览器会话，捕获真实500错误"""
import sys, traceback
sys.path.insert(0, '.')

# 开启详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

from app import app, init_db
init_db()

with app.test_client() as c:
    with app.test_request_context():
        pass
    
    # 登录
    rv = c.post('/login', data={'username': 'admin', 'password': 'admin123'}, follow_redirects=False)
    print(f"登录返回: {rv.status_code}, Location: {rv.headers.get('Location', '')}")
    
    # 访问 /customers/2
    rv2 = c.get('/customers/2', follow_redirects=False)
    print(f"\n/customers/2 状态码: {rv2.status_code}")
    if rv2.status_code != 200:
        content = rv2.data.decode('utf-8', errors='replace')
        print("=== 响应内容（前3000字符）===")
        print(content[:3000])
