APP
===

## Установка
---
1. Клонирование репозитория: git clone https://github.com/ArsenyNovak/lkjh8844.git


2. В репозитории создать файл ".env":  
   SECRET_KEY=your_secret_key  
   DB_USERNAME=your_username  
   DB_PASSWORD=your_password  
     

3. Установить зависимости: pip install -r requirements.txt


4. Настройка и установка базы данных:  
   sudo apt install postgresql # установка postgresql  
   sudo -i -u postgres  
   psql  
   CREATE USER your_username PASSWORD 'your_password'; # создание пользователя  
   CREATE DATABASE flask_db OWNER your_username; # создание базы данных


5. Создание таблицы в БД: python3 init_db.py
6. Запуск приложения:  python3 app.py

   
   

