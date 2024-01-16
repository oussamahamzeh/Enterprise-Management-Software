@echo off
cd /D %~dp0
call venv\Scripts\activate
python get_local_ip.py
python manage.py runserver 0.0.0.0:8000  > nul
