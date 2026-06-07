# 🦷 DentalLite — 口腔诊所轻量化管理系统

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/python-3.9%2B-brightgreen?style=flat-square" alt="python">
  <img src="https://img.shields.io/badge/flask-3.0-orange?style=flat-square" alt="flask">
  <img src="https://img.shields.io/badge/sqlite-WAL%20mode-lightgrey?style=flat-square" alt="sqlite">
  <img src="https://img.shields.io/badge/memory-%3C80MB-success?style=flat-square" alt="memory">
  <img src="https://img.shields.io/badge/license-MIT-informational?style=flat-square" alt="license">
</p>

> **一行命令启动，内存占用不足 80 MB，专为 2G 轻量云服务器设计的口腔诊所全流程管理系统。**

DentalLite 是一套开箱即用的口腔诊所管理系统。它覆盖了诊所日常运营的完整闭环：客户建档 → 诊疗记录 → 回访跟进 → 数据统计，全程无需任何额外数据库服务，一个 SQLite 文件存储全部数据。

前端零依赖，后端极致轻量，可在最低配置的阿里云轻量应用服务器上流畅运行。

[安装部署手册](./安装部署手册.md) · [API 概览](#-api-概览) · [快速开始](#-快速开始) · [常见问题](#-常见问题)

---

**新用户？从这里开始：** [快速开始](#-快速开始)

**部署到生产服务器？** 查看 [安装部署手册](./安装部署手册.md)，包含 Gunicorn + systemd + Nginx + HTTPS 完整配置。

---

## ✨ 功能亮点

| 模块 | 功能 |
|------|------|
| 🏠 **首页看板** | 当日待回访、近 3 天复诊提醒、快捷操作入口 |
| 👤 **客户档案** | 建档/编辑/搜索、标签管理、手机号唯一校验、Excel 导出 |
| 🩺 **诊疗记录** | 主诉 / 诊断 / 治疗方案 / 用药 / 费用 / 医嘱全字段录入、口腔影像附件、打印支持 |
| 📞 **回访跟进** | 创建回访计划、登记回访结果、首页智能提醒 |
| 📊 **数据统计** | 月度就诊趋势、治疗项目分布、收入走势图表、Excel 导出 |
| ⚙️ **系统设置** | 诊所信息、数据字典（治疗项目 / 药品 / 标签）自定义、一键数据库备份下载 |
| 🔐 **权限管理** | 管理员 / 医生两级权限，操作隔离 |

---

## 🏗️ 技术架构

```
┌──────────────────────────────────────────┐
│           浏览器（前端零依赖）              │
│   HTML5 · CSS3 · Vanilla JS · Chart.js   │
└──────────────────┬───────────────────────┘
                   │ HTTP / REST API
┌──────────────────▼───────────────────────┐
│           Python Flask 后端               │
│    路由 · 鉴权 · 业务逻辑 · 38 个 API     │
└──────────────────┬───────────────────────┘
                   │ SQLite WAL
┌──────────────────▼───────────────────────┐
│          SQLite 文件数据库                 │
│     dental.db（无独立进程，随迁易备）       │
└──────────────────────────────────────────┘
```

| 层级 | 技术 | 内存占用 |
|------|------|----------|
| WSGI 服务器 | Gunicorn（2 workers） | ~30 MB |
| Web 框架 | Flask 3.0 | ~20 MB |
| 数据库 | SQLite WAL 模式 | ~5 MB |
| 前端 | 原生 HTML / CSS / JS | 0 MB |
| 图表 | Chart.js（CDN 按需加载） | — |
| **合计** | | **< 80 MB** |

---

## 🚀 快速开始

**运行环境：** Python 3.9+（推荐 3.11）

```bash
# 1. 克隆项目
git clone https://github.com/yourname/dental-lite.git
cd dental-lite

# 2. 安装依赖（约 30 秒）
pip install -r requirements.txt

# 3. 启动
python app.py
```

打开浏览器访问 [http://localhost:5000](http://localhost:5000)

| 账号 | 密码 | 角色 |
|------|------|------|
| `admin` | `admin123` | 管理员（全部权限） |
| `doctor` | `doctor123` | 医生（诊疗 + 客户管理） |

> ⚠️ **安全提醒**：首次登录后请立即在「系统设置」中修改默认密码，并将 `app.py` 第 21 行的 `secret_key` 替换为随机字符串。

---

## 📦 生产部署（阿里云轻量服务器）

推荐使用 **Gunicorn + systemd + Nginx** 组合：

```bash
# 服务器上执行
pip3 install -r requirements.txt gunicorn
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

完整步骤（含 HTTPS、开机自启、定时备份）请查看 👉 **[安装部署手册.md](./安装部署手册.md)**

---

## 📁 项目结构

```
dental-clinic/
├── app.py                 # 主程序（全部路由 + 38 个 API）
├── dental.db              # SQLite 数据库（首次运行自动创建）
├── requirements.txt       # Python 依赖（6 个包）
├── gunicorn_config.py     # Gunicorn 生产配置
├── dental-clinic.service  # systemd 服务文件
├── start.sh               # Linux 一键启动脚本
├── 启动.bat               # Windows 一键启动脚本
├── README.md              # 本文件
├── 安装部署手册.md        # 详细部署文档
├── static/
│   └── uploads/           # 诊疗附件上传目录
└── templates/             # Jinja2 页面模板
    ├── layout.html        # 公共导航布局
    ├── login.html         # 登录页
    ├── index.html         # 首页看板
    ├── customers.html     # 客户列表
    ├── customer_detail.html  # 客户详情 + 档案编辑
    ├── treatments.html    # 诊疗记录列表
    ├── followups.html     # 回访跟进
    ├── stats.html         # 数据统计图表
    └── settings.html      # 系统设置
```

---

## 🔌 API 概览

系统提供 38 个 RESTful API，覆盖全部业务模块：

```
GET/POST   /api/customers            客户列表 / 新建客户
GET/PUT/DELETE /api/customers/:id    获取 / 编辑 / 删除客户
GET        /api/customers/export     导出客户 Excel

GET/POST   /api/treatments           诊疗记录列表 / 新增
GET/PUT    /api/treatments/:id       获取 / 更新诊疗记录
POST       /api/treatments/:id/upload  上传附件
GET        /api/treatments/export    导出诊疗 Excel

GET/POST   /api/followups            回访计划列表 / 新建
PUT        /api/followups/:id        更新回访记录

GET        /api/statistics/overview  统计数据（图表用）

GET/POST   /api/users                用户列表 / 新建用户
PUT        /api/users/:id            更新用户
GET/POST   /api/settings             诊所设置
GET/POST   /api/dict/:category       数据字典
DELETE     /api/dict/:id             删除字典项
POST       /api/change-password      修改密码
GET        /api/backup               下载数据库备份
GET        /api/doctors              医生列表（下拉用）
```

---

## 🔒 安全说明

DentalLite 是内网/私有部署项目，**默认不对公网暴露**。

| 风险项 | 建议 |
|--------|------|
| 默认 `secret_key` | **必须**修改为随机字符串（`python -c "import secrets; print(secrets.token_hex(32))"` 生成） |
| 默认密码 | 首次登录后立即修改 `admin/admin123` |
| HTTP 明文 | 生产环境务必配置 Nginx + SSL 证书（Let's Encrypt 免费） |
| 上传文件 | 已限制类型（jpg/png/gif/pdf/webp）和大小（16 MB），定期清理 `static/uploads/` |
| 数据备份 | 「系统设置 → 数据备份」一键下载，或配置 crontab 定时备份 `dental.db` |

---

## ⚙️ 配置项

核心配置集中在 `app.py` 头部：

```python
# 第 21 行 - 生产环境必须修改为随机值
app.secret_key = 'your-random-secret-key-here'

# 第 31 行 - 附件上传大小限制（默认 16MB）
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# 第 32 行 - 允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'bmp', 'webp'}
```

---

## 🗄️ 数据库

系统使用 **SQLite WAL 模式**，数据库文件为 `dental.db`，首次运行自动创建并写入默认数据。

**数据表：**

| 表名 | 说明 |
|------|------|
| `users` | 用户账号（账号/密码/角色） |
| `customers` | 客户档案（基本信息/标签/就诊统计） |
| `treatments` | 诊疗记录（主诉/诊断/治疗/费用/附件） |
| `followups` | 回访计划与记录 |
| `settings` | 诊所基础信息 |
| `dict_items` | 数据字典（治疗项目/药品/标签等） |

**手动重置管理员密码：**

```bash
python3 - <<'EOF'
import sqlite3
from werkzeug.security import generate_password_hash
conn = sqlite3.connect('dental.db')
conn.execute("UPDATE users SET password_hash=? WHERE username='admin'",
             (generate_password_hash('你的新密码'),))
conn.commit()
conn.close()
print("密码已重置")
EOF
```

---

## 💻 常见问题

**Q：启动报 `ModuleNotFoundError`？**
```bash
pip install -r requirements.txt
```

**Q：端口被占用怎么办？**
```bash
# 修改启动端口（Windows）
python app.py --port 5066

# 或直接修改 app.py 最后一行
app.run(host='0.0.0.0', port=5066)
```

**Q：重启服务后被自动退出登录？**  
原因：Flask 每次启动使用固定 `secret_key`，若 `secret_key` 变化会使旧 Session 失效。清空浏览器 Cookie 后重新登录即可。

**Q：如何数据备份？**  
方式一：登录系统 → 「系统设置」→「数据备份」→ 一键下载 `dental.db`  
方式二：直接拷贝 `dental.db` 文件和 `static/uploads/` 目录

**Q：服务器上内存占用过高？**  
```python
# 修改 gunicorn_config.py
workers = 1   # 从 2 改为 1，节省约 20MB
```

---

## 🛠️ 本地开发

```bash
# 克隆并安装依赖
git clone https://github.com/yourname/dental-lite.git
cd dental-lite
pip install -r requirements.txt

# 以 Debug 模式启动（代码修改后自动重载）
FLASK_DEBUG=1 python app.py

# Windows PowerShell
$env:FLASK_DEBUG=1; python app.py
```

---

## 📋 依赖清单

```
flask==3.0.3          Web 框架
flask-sqlalchemy==3.1.1  ORM（可选扩展用）
flask-login==0.6.3    会话管理
werkzeug==3.0.3       密码加密 / 文件上传
openpyxl==3.1.3       Excel 导出
pillow==10.4.0        图片处理（附件缩略图）
```

---

## 🤝 Contributing

欢迎提交 PR 和 Issue！

- Bug 报告：请附上操作步骤和错误截图
- 功能建议：请描述使用场景和预期效果
- 代码贡献：请确保本地 `python app.py` 能正常启动后再提交 PR

---

## 📄 License

[MIT License](./LICENSE) · 自由使用，保留版权声明即可

---

> 🦷 **DentalLite** · 让每家小诊所都用得上好用的管理工具  
> 技术支持：xingruiqiang@163.com
