FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV FLASK_APP=app
ENV FLASK_ENV=production

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]


