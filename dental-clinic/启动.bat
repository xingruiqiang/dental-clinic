@echo off
chcp 65001
echo ================================================
echo  口腔诊所轻量化管理系统
echo ================================================
cd /d "%~dp0"

echo 检查Python环境...
python --version 2>nul
if errorlevel 1 (
    echo [错误] 未找到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

echo 安装依赖包...
pip install -r requirements.txt -q

echo 启动系统...
echo.
echo 访问地址: http://localhost:5000
echo 默认账号: admin
echo 默认密码: admin123
echo.
echo 按 Ctrl+C 停止服务
echo ================================================
python app.py
pause
