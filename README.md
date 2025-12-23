# Mortgage Calculator (Ипотечный калькулятор)

Веб-приложение на Flask для расчёта ипотеки с использованием CI/CD в GitHub Actions.

## Локальный запуск

```bash
cd /Users/alexseyinyatkin/Desktop/sfu5/kubernetis/lab3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8000
```

Откройте `http://localhost:8000` в браузере.

## Тесты

```bash
pytest -v
```

## Docker

```bash
docker build -t mortgage-app:latest .
docker run -d -p 8000:8000 --name mortgage-app mortgage-app:latest
```

## CI/CD (GitHub Actions)

- Пайплайн состоит из этапов: `test` → `lint` → `build` → `deploy`.
- Тесты и линтер выполняются на GitHub-hosted runners (Ubuntu).
- Сборка Docker-образа выполняется на GitHub-hosted runner.
- Деплой выполняется на self-hosted runner на продуктовой ВМ (должен быть установлен Docker).

### Настройка self-hosted runner для деплоя

1. На продуктовой ВМ установите Docker:
   ```bash
   curl -fsSL https://get.docker.com | sudo sh
   ```

2. Добавьте self-hosted runner в репозиторий GitHub:
   - Перейдите в Settings → Actions → Runners → New self-hosted runner
   - Следуйте инструкциям для установки и регистрации runner'а
   - Runner должен иметь тег `self-hosted` (по умолчанию)

3. После настройки runner'а, при push в ветку `main` будет автоматически запускаться деплой.


