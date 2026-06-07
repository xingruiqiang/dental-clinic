# 🦷 口腔诊所轻量化管理系统

> 专为 **2G内存轻量云服务器** 设计的口腔诊所管理解决方案

## 📋 功能概览

| 模块 | 功能 |
|------|------|
| 🏠 **首页看板** | 今日待回访提醒、近3天复诊提醒、快捷入口 |
| 👤 **客户档案** | 建档/编辑/查询、标签管理、手机号唯一校验、Excel导出 |
| 🩺 **诊疗记录** | 完整录入（主诉/诊断/治疗/用药/费用/医嘱）、历史追溯、附件上传、打印 |
| 📞 **回访跟进** | 回访计划创建、回访记录登记、首页智能提醒 |
| 📊 **数据统计** | 月度趋势/治疗项目/就诊类型/收入图表、Excel导出 |
| ⚙️ **系统设置** | 诊所信息、数据字典（治疗项目/药品/标签）、数据备份下载 |
| 🔐 **权限管理** | 管理员/医生两级权限，操作隔离 |

## 🏗️ 技术架构

```
┌──────────────────────────────────────┐
│           前端（零依赖）               │
│  HTML5 + CSS3 + Vanilla JS + Chart.js │
└──────────────┬───────────────────────┘
               │ HTTP
┌──────────────▼───────────────────────┐
│          Python Flask 后端            │
│    路由 / 鉴权 / 业务逻辑 / API       │
└──────────────┬───────────────────────┘
               │ SQLite
┌──────────────▼───────────────────────┐
│         SQLite 文件数据库（无独立进程） │
│             dental.db                 │
└──────────────────────────────────────┘
```

| 层级 | 技术选型 | 内存占用 |
|------|----------|----------|
| Web服务器 | Gunicorn（2 workers） | ~30MB |
| 后端框架 | Flask 3.0 | ~20MB |
| 数据库 | SQLite（WAL模式） | ~5MB |
| 前端 | 原生 HTML/CSS/JS | 0MB |
| 图表 | Chart.js（CDN） | 按需加载 |
| **总计** | | **≈ 50-80MB** |

## 🚀 快速启动（本地）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 启动服务
python app.py

# 3. 浏览器访问
http://localhost:5000
```

**默认账号**：`admin` / `admin123`

## 📦 部署指南

阿里云 Linux 轻量服务器部署请查看：**[安装部署手册.md](./安装部署手册.md)**

## 📁 项目结构

```
dental-clinic/
├── app.py                 # 主程序（所有 API + 路由）
├── dental.db              # SQLite 数据库（自动创建）
├── requirements.txt       # Python 依赖
├── start.sh               # Linux 启动脚本
├── 启动.bat               # Windows 启动脚本
├── dental-clinic.service  # systemd 服务配置
├── README.md              # 本文件
├── 安装部署手册.md        # 安装部署手册
├── static/
│   └── uploads/           # 附件上传目录
└── templates/             # Jinja2 页面模板（10个）
    ├── layout.html        # 公共布局
    ├── login.html         # 登录页
    ├── index.html         # 首页看板
    ├── customers.html     # 客户列表
    ├── customer_detail.html  # 客户详情/档案
    ├── treatments.html    # 诊疗记录
    ├── followups.html     # 回访跟进
    ├── stats.html         # 数据统计
    ├── settings.html      # 系统设置
    └── export.html        # 导出页
```

## 🔧 自定义配置

### 修改端口
编辑 `dental-clinic.service` 或启动命令中的端口号。

### 修改管理员密码
```sql
-- 进入数据库
sqlite3 dental.db

-- 修改密码（密码会经过 werkzeug 加密）
UPDATE users SET password_hash='新密码hash' WHERE username='admin';
```

### 添加数据字典项
登录后进入「系统设置」→「数据字典」→ 添加/编辑。

## ⚠️ 注意事项

1. **secret_key**：生产环境请修改 `app.py` 第21行的 `secret_key` 为随机字符串
2. **数据备份**：定期备份 `dental.db` 文件和 `static/uploads/` 目录
3. **附件存储**：上传文件保存在 `static/uploads/`，建议定期清理
4. **HTTPS**：生产环境建议配置 Nginx + SSL 证书

## 📄 许可

内部使用项目
