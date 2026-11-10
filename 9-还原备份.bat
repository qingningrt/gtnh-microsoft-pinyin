@echo off
chcp 936 >nul
setlocal enabledelayedexpansion
cd /d "%~dp0"
title GTNH 简拼 - 还原备份

set "LEX=%APPDATA%\Microsoft\InputMethod\Chs\ChsPinyinEUDPv1.lex"
if defined GTNH_LEX set "LEX=%GTNH_LEX%"

if not exist "backup\*.lex.bak" (
  echo [X] backup 目录里没有备份文件，无法还原。
  pause
  exit /b 1
)

set "BAK="
for /f "delims=" %%f in ('dir /b /o-d "backup\*.lex.bak"') do (
  if not defined BAK set "BAK=backup\%%f"
)
echo 将用以下备份覆盖当前短语文件:
echo   备份: %BAK%
echo   目标: %LEX%
echo.
copy /y "%BAK%" "%LEX%" >nul
if errorlevel 1 (
  echo [X] 还原失败，请手动把上述备份复制到目标路径。
  pause
  exit /b 1
)
echo 已还原。切换一次输入法后生效。
pause
