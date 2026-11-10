@echo off
chcp 936 >nul
setlocal
cd /d "%~dp0"
title GTNH 简拼 - 一键导入

set "LEX=%APPDATA%\Microsoft\InputMethod\Chs\ChsPinyinEUDPv1.lex"
if defined GTNH_LEX set "LEX=%GTNH_LEX%"

echo ============================================
echo   GTNH 微软拼音简拼词库
echo ============================================
echo 目标文件: %LEX%
echo.

if not exist "%LEX%" (
  echo [X] 找不到微软拼音的数据文件。
  echo     请确认系统里装的是"微软拼音"并至少使用过一次。
  echo     如果路径不同，可设置环境变量 GTNH_LEX 指向你的 .lex 文件。
  echo.
  pause
  exit /b 1
)
if not exist "phrases.txt" (
  echo [X] 当前目录缺少 phrases.txt
  pause
  exit /b 1
)
if not exist "tools\PinyinLexTool.exe" (
  echo [X] 缺少 tools\PinyinLexTool.exe
  echo.
  echo     请到以下地址下载 v1.0.1 的 PinyinLexTool.exe：
  echo     https://github.com/mchudie/PinyinLexTool/releases
  echo     放到本目录的 tools\ 文件夹里，再重新运行本脚本。
  echo.
  pause
  exit /b 1
)

for /f "delims=" %%a in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "TS=%%a"
if not exist "backup" mkdir "backup"
set "BAK=backup\ChsPinyinEUDPv1.%TS%.lex.bak"
copy /y "%LEX%" "%BAK%" >nul
if errorlevel 1 (
  echo [X] 备份失败，已中止，未做任何修改。
  pause
  exit /b 1
)
echo [1/3] 已备份: %BAK%
echo.

echo [2/3] 正在导入短语...
echo.
"tools\PinyinLexTool.exe" import "phrases.txt" --lex "%LEX%" --no-backup --verbose
if errorlevel 1 (
  echo.
  echo [i] 直接写入失败，改用副本流程...
  copy /y "%LEX%" "_work.lex" >nul
  "tools\PinyinLexTool.exe" import "phrases.txt" --lex "_work.lex" --no-backup --verbose
  if errorlevel 1 (
    echo [X] 导入失败，原文件未改动。
    pause
    exit /b 1
  )
  copy /y "_work.lex" "%LEX%" >nul
  if errorlevel 1 (
    echo [X] 覆盖原文件失败，原文件未改动。
    pause
    exit /b 1
  )
  del /q "_work.lex" >nul 2>nul
)
echo.
echo [3/3] 完成。
echo.
echo 请切换一次输入法让它重新加载：
echo     Alt+Shift 或 Win+空格，切到英文再切回来
echo 然后在记事本里输入 qys，应出现"氢元素"。
echo 想撤销就双击 9-还原备份.bat
echo.
pause
