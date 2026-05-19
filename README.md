# Админ-панель аналитики колледжа (Instagram + 2GIS)

Flask-приложение для мониторинга репутации и контент-эффективности колледжа
«Инновационный Технический колледж» в социальных сетях и 2GIS.

## Что внутри дашборда
- KPI: рейтинг 2GIS, подписчики IG, ER, охват
- Динамика положительных / отрицательных / нейтральных отзывов
- Распределение рейтингов 2GIS
- Топ-темы позитива и негатива
- Сравнение с 4 конкурентами (рейтинг, отзывы, engagement)
- Рост подписчиков Instagram, структура контента
- Топ публикаций IG
- Авто-сформированные выводы и рекомендации по улучшению

## Локальный запуск
```bash
pip install -r requirements.txt
python app.py
# открой http://localhost:5000
```

## Деплой на GitHub
```bash
git init
git add .
git commit -m "Initial commit: college analytics dashboard"
git branch -M main
git remote add origin https://github.com/<your-username>/college-dashboard.git
git push -u origin main
```

## Деплой на PythonAnywhere

1. Создай аккаунт https://www.pythonanywhere.com
2. **Consoles → Bash:**
   ```bash
   git clone https://github.com/<your-username>/college-dashboard.git
   cd college-dashboard
   pip3.10 install --user -r requirements.txt
   ```
3. **Web → Add a new web app → Manual configuration → Python 3.10**
4. В разделе **Code** укажи:
   - Source code: `/home/<user>/college-dashboard`
   - Working directory: `/home/<user>/college-dashboard`
5. Открой WSGI configuration file и замени содержимое на:
   ```python
   import sys
   path = '/home/<user>/college-dashboard'
   if path not in sys.path:
       sys.path.insert(0, path)
   from app import app as application
   ```
6. Нажми **Reload** — приложение доступно по `https://<user>.pythonanywhere.com`

## Структура
```
college_dashboard/
├── app.py              # Flask-роуты
├── data.py             # Мок-данные и логика рекомендаций
├── requirements.txt
├── templates/
│   └── index.html      # Дашборд
└── static/
    └── style.css
```

## Замена мок-данных на реальные
В `data.py` функция `get_dashboard_data()` возвращает словарь.
Подключи Instagram Graph API и 2GIS Catalog API, заменив генерацию
случайных значений на реальные вызовы — структура ответа сохранится,
дашборд работать продолжит.
