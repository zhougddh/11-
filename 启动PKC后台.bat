@echo off

:: 一键启动PKC音色管理后台

echo 正在启动PKC音色管理后台...
echo 服务地址: http://127.0.0.1:39903
echo 登录地址: http://127.0.0.1:39903/login
echo 用户名: 1585546839
echo 密码: 1585546839@qq.com
echo.

echo 请按任意键开始启动服务...
pause > nul

:: 检查Python是否安装
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未找到Python，请先安装Python 3.7+
    pause
    exit /b 1
)

:: 检查依赖是否安装
echo 检查依赖...
pip list | findstr "Flask" > nul 2>&1
if %errorlevel% neq 0 (
    echo 安装依赖...
    pip install Flask
    if %errorlevel% neq 0 (
        echo 错误: 依赖安装失败
        pause
        exit /b 1
    )
)

echo 启动服务...
python main.py

pause