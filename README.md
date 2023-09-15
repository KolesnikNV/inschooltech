## Установка

1. Склонируйте репозиторий на свой компьютер:

```git clone https://github.com/KolesnikNV/inschooltech.git```

2. Установите необходимые зависимости:

```pip install -r requirements.txt или poetry install```

3. Примените миграции:

```python manage.py migrate```

4. Запустите сервер:

```python manage.py runserver```

Теперь ваш проект должен быть доступен по адресу http://localhost:8000/.

5. Или проект можно запустить через Docker используя ```docker-compose up -d```

### API Endpoints

1. **Аутентификация**: Для аутентификации и управления пользователями используются [Djoser](https://djoser.readthedocs.io/en/latest/). Вы можете получить токен аутентификации, отправив запрос к `/auth/token/login/`.

2. **Лаборатории**: Вы можете получить список лабораторий по адресу `/labs/` и просмотреть детали лаборатории по адресу `/labs/{lab_id}/`.

3. **Тесты**: Вы можете получить список тестов по адресу `/tests/` и просмотреть детали теста по адресу `/tests/{test_id}/`.

4. **Индикаторы**: Вы можете получить список индикаторов по адресу `/indicators/` и просмотреть детали индикатора по адресу `/indicators/{indicator_id}/`.

5. **Метрики**: Вы можете получить список метрик по адресу `/metrics/` и просмотреть детали метрики по адресу `/metrics/{metric_id}/`.

6. **Оценки**: Вы можете получить список оценок по адресу `/scores/` и просмотреть детали оценки по адресу `/scores/{score_id}/`.

7. **Справочники**: Вы можете получить список справочников по адресу `/references/` и просмотреть детали справочника по адресу `/references/{reference_id}/`.
