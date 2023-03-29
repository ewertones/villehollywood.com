FROM python:3.11.1-slim
ENV PYTHONUNBUFFERED True
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app /app
WORKDIR /app
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app