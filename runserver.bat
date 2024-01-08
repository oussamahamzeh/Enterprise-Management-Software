@echo off
cd /D %~dp0
call venv\Scripts\activate
python manage.py runserver
