TASKKILL /IM "SAVED.exe" 
cd /d "%~dp0..\..\SAVED"
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)