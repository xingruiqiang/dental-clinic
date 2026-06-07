#!/bin/bash
# 口腔诊所轻量化管理系统 Linux启动脚本
# 适用于 2G内存云服务器

echo "================================================"
echo " 口腔诊所轻量化管理系统"
echo "================================================"

# 进入项目目录
cd "$(dirname "$0")"

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "[错误] 未找到Python3，请先安装: sudo apt install python3 python3-pip"
    exit 1
fi

# 安装依赖
echo "安装依赖包..."
pip3 install -r requirements.txt -q

# 创建上传目录
mkdir -p static/uploads

echo ""
echo "系统启动中..."
echo "访问地址: http://$(hostname -I | awk '{print $1}'):5000"
echo "本地访问: http://localhost:5000"
echo "默认账号: admin  密码: admin123"
echo ""
echo "按 Ctrl+C 停止服务"
echo "================================================"
python3 app.py
