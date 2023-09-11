@echo off
@REM pyinstaller.exe --onefile --clean --hidden-import=pywin32 --name "PST Windows" --uac-admin --icon=resources\icon.ico .\main.py
pyinstaller.exe --onedir --clean --hidden-import=terminaltables --name "PST Windows" --uac-admin --icon=resources\icon.ico --add-data=".\wdckit\*;wdckit" .\main.py

@REM Build cleanup
echo "Cleaning-up CWD"
rd build /s /q
del "PST Windows.spec" /f /q
move /y dist\"PST Windows" .
rd dist /s /q
rd __pycache__ /s /q
timeout 2 /nobreak

@REM # Compress to ZIP
echo Creating ZIP
tar -a -c -C "PST Windows" -f "PST Windows.zip" "*"
timeout 1 /nobreak
rd "PST Windows" /s /q

echo Build Success
pause
@echo on