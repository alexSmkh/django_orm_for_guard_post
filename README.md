# Пульт охраны 

Сервис для отслеживания визитов посетителей, прошедших через пульт охраны. 

Сайт состоит из нескольких страниц, на которых можно узнать: 
* информацию по пропускам 
* о посетителях, находящихся на территории охраняемого объекта
* всю историю посещений по каждому пропуску


### Как настроить
Должен быть установлен `python3`. Затем используйте `pip`(или `pip3`, если есть конфликт с `python2`) для установки зависимостей:
```bash
pip install -r requirements.txt
```

Создайте файл `.env` в одной директории с `main.py`  и запишите в него данные вашей БД:
```txt
HOST=...
PORT=...
NAME=...        
USER=...
PASSWORD=...
SECRET_KEY=...
```

### Как запустить 

```bash
python manage.py runserver
```

