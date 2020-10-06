@ECHO OFF
start cmd.exe /C "pip install django && cd D:\D1\ && D:"
start cmd.exe /C "pip install django-widget-tweaks && cd D:\D1\ && D:"
start cmd.exe /C "pip install folium && cd D:\D1\ && D:"
start cmd.exe /C "python manage.py runserver && cd D:\D1\ && D:"


start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "127.0.0.1:8000/admin"
start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "127.0.0.1:8000/"