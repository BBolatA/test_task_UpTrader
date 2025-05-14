treeMenu
Древовидное меню на Django (тестовое задание).

Возможности
- Хранение меню и пунктов в БД
- Редактирование через стандартную админку
- Вывод через template-tag `{% draw_menu 'name' %}`
- Один SQL-запрос на меню
- Подсветка активного пункта и автo-раскрытие ветки
- Несколько меню на одной странице (по `name`)
- Демоменю `main_menu` (сайдбар) и `footer_menu` (футер)

Технологии
- Python 3.10.6
- Django 5.2
- Bootstrap 5 (CDN)
- SQLite (по умолчанию)

Запуск
```bash
git clone https://github.com/BBolatA/test_task_UpTrader.git
cd test_task
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
python manage.py migrate 
python manage.py runserver
